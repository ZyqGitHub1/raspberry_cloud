from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required
from .. models import User
from . import auth

@auth.route('/login',methods=['GET', 'POST'])
def login():
	data = request.json
	user_name = data[name]
	user_password = data[password]
	remember = data[remember]
	user = User.query.filter_by(name = user_name).first()
	if user is not None and user.verfy_password(user_passsword):
		loggin_user(user, remember)
		return redirect(request.args.get('next') or url_for('main.console'))
	else:
		result = {
		'successful':false,
		}
		return jsonify(result)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
	pass