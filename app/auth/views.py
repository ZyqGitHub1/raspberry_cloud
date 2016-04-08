# -*- coding:utf-8 -*-
from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required,current_user
from .. models import User
from . import auth
from .. import db
from .. email import send_email

def noneIfEmptyString(value):
	if value == '':
		return None
	return value

'''
@auth.before_app_request
def before_request():
	if current_user.is_authenticated \
			and not current_user.confirmed \
			and request.endpoint[:5] != 'auth.' \
			and request.endpoint != 'static':
		return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous or current_user.confirmed:
		return redirect(url_for('main.index'))
	return render_template('auth/unconfirmed.html')
'''

#登陆路由
@auth.route('/login',methods=['GET', 'POST'])
def login():
	data = request.form
	print data
	user_name = data.get('username')
	user_password = data.get('password')
	remember = data.get('rememberMe')
	user = User.query.filter_by(username = user_name).first()
	if user is not None and user.verify_password(user_password):
		login_user(user, remember)
		result = {
		'successful':True,
		'url': request.args.get('next') or url_for('main.main')
		}
		return jsonify(result)
	else:
		result = {
		'successful':False,
		}
		return jsonify(result)

#注销路由
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))

#注册路由
@auth.route('/register', methods=['GET', 'POST'])
def register():
	data = request.form
	print data
	user_name = noneIfEmptyString(data.get('username'))
	user_email = noneIfEmptyString(data.get('email'))
	user_password1 = noneIfEmptyString(data.get('password'))
	user_password2 = noneIfEmptyString(data.get('repassword'))
	user = User.query.filter_by(username = user_name).first()
	print user_name
	if user_name is None:
		result = {
		'successful': False,
		'error': 1,
		}
		return jsonify(result)
	elif user is not None:
		result = {
		'successful': False,
		'error': 2,
		}
		return jsonify(result)
	elif user_password1 is None:
		result = {
		'successful': False,
		'error': 3,
		}
		return jsonify(result)
	elif user_password1 != user_password1:
		result = {
		'successful': False,
		'error': 4,
		}
		return jsonify(result)
	else:
		user = User(username = user_name,
			email = user_email,
			password = user_password1)
		db.session.add(user)
		db.session.commit()
		token = user.generate_confirmation_token()
		send_email(user.email, 'Confirm Your Account',
				   'auth/email/confirm', user=user, token=token)
		result = {
		'successful':True,
		'url': url_for('main.index'),
		'msg': 'A confirmation email has been sent to you by email.'
		}
		return jsonify(result)
	

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		result = {
		'successful':True,
		'url': url_for('main.main')
		}
		return jsonify(result)
	if current_user.confirm(token):
		result = {
		'successful':True,
		'msg': 'You have confirmed your account. Thanks!'
		}
		return jsonify(result)
	else:
		result = {
		'successful':True,
		'url': url_for('main.main'),
		'msg': 'The confirmation link is invalid or has expired.'
		}
	return jsonify(result)


@auth.route('/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_email(current_user.email, 'Confirm Your Account',
			   'auth/email/confirm', user=current_user, token=token)
	result = {
		'successful':True,
		'url': url_for('main.index'),
		'msg': 'A new confirmation email has been sent to you by email.'
		}
	return jsonify(result)

@auth.route('/changeusername', methods=['GET', 'POST'])
@login_required
def change_username():
	data = request.form
	print data
	new_username = data.get('new_username')
	user = User.query.filter_by(new_username).first()
	if user:
		result = {
		'successful':False,
		'error':1
		}
		return json(result)
	elif(new_username == None):
		result = {
		'successful':False,
		'error':2
		}
		return json(result)
	else:
		current_user.username = new_username
		db.sessin.add(current_user)
		result = {
		'successful':True,
		'url':url_for('main.mian')
		}
		return json(result)

@auth.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
	data = request.form
	print data
	oldpassword = noneIfEmptyString(data.get('oldpassword'))
	password = noneIfEmptyString(data.get('password'))
	repassword = noneIfEmptyString(data.get('repassword'))
	if not current_user.verify_password(oldpassword):
		result = {
		'successful':False,
		'error': 1
		}
		return jsonify(result)
	elif(password != repassword):
		result = {
				'successful':False,
				'error': 2
				}
		return jsonify(result)
	elif(password == None):
		result = {
				'successful':False,
				'error': 3
				}
		return jsonify(result)
	else:
		current_user.password = password
		db.session.add(current_user)
		result = {
		'successful':True,
		'url': url_for('main.index'),
		}
		return jsonify(result)

@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset Your Password',
                       'auth/email/reset_password',
                       user=user, token=token,
                       next=request.args.get('next'))
        flash('An email with instructions to reset your password has been '
              'sent to you.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return redirect(url_for('main.index'))
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)

@auth.route('/changeemail', methods=['GET', 'POST'])
@login_required
def change_email_request():
	data = request.form
	if current_user.verify_password(data.get(password)):
		new_email = data.get(new_email)
		token = current_user.generate_email_change_token(new_email)
		send_email(new_email, 'Confirm your email address',
				   'auth/email/change_email',
				   user=current_user, token=token)
		result = {
		'successful':True,
		'url':url_for('main.main')
		'msg':'一封确认邮件已经发送到您的新邮箱，3秒后将为您跳转到主页'
		}
		return json(result)
	else:
		result = {
		'successful':False,
		'msg':'错误的邮箱或密码'
		}
		return json(result)

@auth.route('/changeemail/<token>')
@login_required
def change_email(token):
	if current_user.change_email(token):
		flash('Your email address has been updated.')
	else:
		flash('Invalid request.')
	return redirect(url_for('main.index'))