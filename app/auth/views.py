from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required
from .. models import User
from . import auth
from .. import db

def noneIfEmptyString(value):
    if value == '':
        return None
    return value

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

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))

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
		result = {
		'successful':True,
		'url': url_for('main.index')
		}
		return jsonify(result)
