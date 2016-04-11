from flask import render_template,redirect,request,url_for,flash,jsonify,json
from flask.ext.login import login_user,logout_user,login_required
from .. models import User,Electrical,Pin
from . import control
from .. import db

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

@control.route('/query/electrical',methods=['GET', 'POST'])
@login_required
def query_electrical():
    electrical = Electrical.query.all()
    electricalList=[]
    for tmp in electrical:
        electricalList.append({'electname':tmp.electrical_name,'pin':tmp.pin_id, 'remark':tmp.remark,\
         'status':Pin.query.filter_by(id = tmp.pin_id).status})
    result = {
            'successful':True,
            'data':{
                'electrical': electricalList,
            }
        }
    return jsonify(result)



