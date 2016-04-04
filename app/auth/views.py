from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required
from .. models import User
from . import auth

@auth.route('/login',methods=['GET', 'POST'])
def login():
	data = request.form
	print data
	user_name = data.get('username')
	user_password = data.get('password')
	remember = data.get('rememberMe')
	user = User.query.filter_by(username = user_name).first()
	if user is not None and user.verfy_password(user_passsword):
		loggin_user(user, remember)
		return redirect(request.args.get('next') or url_for('main.console'))
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
	user_name = data.get('username')
	user_email = data.get('email')
	user_password1 = data.get('password')
	user_password2 = data.get('repassword')
	user = User.query.filter_by(username = user_name).first()
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
		return redirect(url_for('main.index'))
