from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required
from .. models import *
from . import control
from .. import db

def noneIfEmptyString(value):
	if value == '':
		return None
	return value

# @control.route('/out',methods=['GET', 'POST'])
# @login_required
# def out():
# 	data = request.form
# 	print data
# 	pin_number = data.get('pin_number')
# 	id = int(pin_number)
# 	GPIO.setmode(GPIO.BCM)
# 	if request.form['turn'] == "on":
# 		GPIO.setup(id,GPIO.OUT)
# 		GPIO.output(id,True)
# 	if request.form['turn'] == "off":
# 		GPIO.setup(id,GPIO.OUT)
# 		GPIO.output(id,False)

@control.route('/add_electrical', methods=['GET', 'POST'])
@login_required
def add_electricals():
	data = request.form
	print data
	electrical_name = noneIfEmptyString(data.get('electrical_name'))
	remark = noneIfEmptyString(data.get('remark'))
	status = noneIfEmptyString(data.get('status'))
	try:
		electrical = Electrical(electrical_name=electrical_name,
								pin_id=Pin.query_by(useable=True).first().bcm_id,
								remark=remark)
		db.session.add(electrical)
		result = {
		'successful': True
		}
	except:
		if(electrical_name==None):
			result = {
			'successful': False,
			'error': 0
			}
		else:
			result = {
			'successful': False,
			'error': 1
			}
	finally:
		return jsonify(result)