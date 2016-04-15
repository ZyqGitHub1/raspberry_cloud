#import RPi.GPIO as GPIO
from .. models import Electrical,Pin
from .. import db


def gpio_change(id,status):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(id,GPIO.OUT)
	try:
		if status == True:
			GPIO.output(id,True)
			Pin.query.filter_by(bcm_id=id).first().status = 1
		if status == False:
			GPIO.output(id,False)
			Pin.query.filter_by(bcm_id=id).first().status = 1
		result = {'status':True}
	except Exception as e:
		result = {'status':True,'error':e}
	finally:
		return result
