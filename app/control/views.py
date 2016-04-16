from flask import render_template,redirect,request,url_for,flash,jsonify,json,Response
from flask.ext.login import login_user,logout_user,login_required
from .. models import *
from . import control
from .. import db
from camera_pi import *
import threading
import time, datetime
from mygpio import *
from celery import Celery
import os
from t_c import *


def noneIfEmptyString(value):
    if value == '':
        return None
    return value

def stringToBool(value):
    if value == u'true':
        return True
    if value == u'false':
        return False
    else:
        return None

@control.route('/switch',methods=['GET', 'POST'])
@login_required
def switch():
    data = request.form
    print data
    pin_id = noneIfEmptyString(data.get('pin_id'))
    status = stringToBool(data.get('status'))
    gpio_change(int(pin_id), status)
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


@control.route('/query_clock',methods=['GET', 'POST'])
@login_required
def query_clock():
    clock = Clock.query.all()
    clockList=[]
    for tmp in clock:
        clockList.append({'electrical_name':tmp.electrical_name,
                        'pin':tmp.pin_id, 
                        'time':tmp.clock_time,
                        'remark':tmp.remark,
                        'status':tmp.status})
    print clockList
    result = {
            'successful':True,
            'data':{
                'clockList': clockList
            }
        }
    return jsonify(result)

@control.route('/timer',methods=['GET', 'POST'])
@login_required
def timer():
    data = request.form
    electrical_name = noneIfEmptyString(data.get('electrical_name'))
    print electrical_name
    clock_time = int(data.get('date')) / 1000
    status = stringToBool(data.get('checked'))
    remark = Electrical.query.filter_by(electrical_name=electrical_name).first().remark
    pin_id = Electrical.query.filter_by(electrical_name=electrical_name).first().pin_id
    clock = Clock(electrical_name=electrical_name,
                  pin_id=pin_id,
                  clock_time=clock_time,
                  status=status,
                  remark=remark)
    db.session.add(clock)
    task = mygpio_task.apply_async(args=[pin_id, status], countdown= int(clock_time-int(time.time())))
    result = {
    'successful':True
    }
    return jsonify(result)

@control.route('/delete_clock', methods=['GET', 'POST'])
@login_required
def delete_clock():
	data = request.form
	electrical_name = data.get('electrical_name')
	clock_time = data.get('clock_time')
	clock = Clock.query.filter_by(electrical_name=electrical_name,
								  clock_time=clock_time).first()
	db.session.delete(clock)
	result = {
	'successful':True
	}
	return jsonify(result)

@control.route('/upload_temperature', methods=['GET', 'POST'])
@login_required
def upload_temperature():
	data = request.json
	time = int(data.get('time'))
	temperature = float(data.get('temperature'))
	humidity = float(data.get('humidity'))
	tmp = Temperature(time=time,
					  temperature=temperature,
					  humidity=humidity)
	db.session.add(tmp)
	result = {
	'successful':True
	}
	return jsonify(result)

@control.route('/temperature_chart', methods=['GET', 'POST'])
@login_required
def temperature_chart():
	data = request.form
	starttime = noneIfEmptyString(data.get('start_time'))
	endtime = noneIfEmptyString(data.get('end_time'))
	if(starttime==None or endtime==None):
		result = {
		'successful':False,
		'error':0
		}
		return jsonify(result)
	elif starttime >= endtime:
		result = {
		'successful':False,
		'error':1
		}
		return jsonify(result)
	else:
		start_time = int(starttime)
		end_time = int(endtime)
		temperatureList = Temperature.query.filter(and_(time>start_time, 
						   time<end_time).order_by(time))
		result = {
		'successful':True,
		'data':{
			'temperatureList':temperatureList
			}
		}
		return jsonify(result)
