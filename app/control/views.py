from flask import render_template,redirect,request,url_for,flash,jsonify,json,Response
from flask.ext.login import login_user,logout_user,login_required
from .. models import User,Electrical,Pin
from . import control
from .. import db
from camera_pi import *
from threading import Timer
import time, datetime

def noneIfEmptyString(value):
	if value == '':
		return None
	return value


@control.route('/switch',methods=['GET', 'POST'])
@login_required
def switch():
	data = request.form
	print data
	pin_id = noneIfEmptyString(data.get('pin_id'))
	id = int(pin_number)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(id,GPIO.OUT)
	if request.form['turn'] == "on":
		GPIO.output(id,True)
	if request.form['turn'] == "off":
		GPIO.output(id,False)
	result = {
		'successful':True,
	}
	return jsonify(result)

@control.route('/query_electrical',methods=['GET', 'POST'])
@login_required
def query_electrical():
	electrical = Electrical.query.all()
	electricalList=[]
	for tmp in electrical:
		electricalList.append({'electrical_name':tmp.electrical_name,
							   'pin':tmp.pin_id, 
							   'remark':tmp.remark,
							   'status':Pin.query.filter_by(bcm_id = tmp.pin_id).first().status})
	print electricalList
	result = {
			'successful':True,
			'data':{
				'electricalList': electricalList
			}
		}
	return jsonify(result)

@control.route('/add_electrical', methods=['GET', 'POST'])
@login_required
def add_electricals():
	data = request.form
	print data
	electrical_name = noneIfEmptyString(data.get('electrical_name'))
	remark = noneIfEmptyString(data.get('remark'))
	status = noneIfEmptyString(data.get('status'))
	if(electrical_name == None):
		result = {
		'successful': False,
		'error': 0
		}
		return jsonify(result)
	elif(Electrical.query.filter_by(electrical_name=electrical_name).first()):
		result = {
		'successful': False,
		'error': 1
		}
		return jsonify(result)
	elif(Pin.query.filter_by(useable=True).first()==None):
		result = {
		'successful': False,
		'error': 2
		}
		return jsonify(result)
	else:
		electrical = Electrical(electrical_name=electrical_name,
								pin_id=Pin.query.filter_by(useable=True).first().bcm_id,
								remark=remark)
		db.session.add(electrical)
		Pin.query.filter_by(useable=True).first().useable = False
		result = {
		'successful': True
		}	
		return jsonify(result)

@control.route('/delete_electrical', methods=['GET', 'POST'])
@login_required
def delete_electrical():
	data = request.form
	print data
	electrical_name = noneIfEmptyString(data.get('electrical_name'))
	electrical = Electrical.query.filter_by(electrical_name=electrical_name).first()
	if(electrical_name):
		Pin.query.filter_by(bcm_id=electrical.pin_id).first().useable = 1
		db.session.delete(electrical)
	result = {
	'successful': True
	}
	return jsonify(result)


@control.route('/video_feed')
@login_required
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @control.route('/timer')
# @login_required
# def timer_switch(, status):


# def timer():
# 	data = request.form
# 	electrical_name = data.noneIfEmptyString(get('electrical_name'))
# 	end_time = float(data.noneIfEmptyString(get('time')))
# 	start_time = time.mktime(datetime.datetime.now().timetuple())
# 	time = start_time - end_time
# 	timer = threading.Timer(time, timer_switch)
# 	timer.start()