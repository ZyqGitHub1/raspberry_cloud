from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required
from .. models import User
from . import control
from .. import db

def noneIfEmptyString(value):
	if value == '':
		return None
	return value

@control.route('/out',methods=['GET', 'POST'])
@login_required
def out():
	data = request.form
	print data
	pin_number = data.get('pin_number')
	id = int(pin_number)
	GPIO.setmode(GPIO.BOARD)
	if request.form['turn'] == "on":
		GPIO.setup(id,GPIO.OUT)
		GPIO.output(id,True)
	if request.form['turn'] == "off":
		GPIO.setup(id,GPIO.OUT)
		GPIO.output(id,False)

