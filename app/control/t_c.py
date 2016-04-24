import urllib2
import json
from celery import Celery

app = Celery(__name__,include=['app.control.views'])
app.conf.update(
    BROKER_URL = 'redis://localhost:6379/0',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1',
#     CELERY_TASK_SERIALIZER = 'json',
#     CELERY_RESULT_SERIALIZER = 'json',
#     CELERY_ACCEPT_CONTENT=['json'],
#     CELERY_TIMEZONE = 'Europe/Oslo',
#     CELERY_ENABLE_UTC = True,
)

@app.task
def mygpio_task(id,status):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(id,GPIO.OUT)
    try:
        if status == True:
            GPIO.output(id,True)
            Pin.query.filter_by(bcm_id=id).first().status = 1
            print 'True'
        if status == False:
            GPIO.output(id,False)
            Pin.query.filter_by(bcm_id=id).first().status = 1
            print 'False'
        result = {'status':True}
    except Exception as e:
        result = {'status':True,'error':e}
    finally:
        return result


@app.task
def get_temp(stime):
    while True:
        channel = 22
        data = []
        j = 0
        
        GPIO.setmode(GPIO.BCM)
        
        time.sleep(1)
        
        GPIO.setup(channel, GPIO.OUT)
        
        GPIO.output(channel, GPIO.LOW)
        time.sleep(0.02)
        GPIO.output(channel, GPIO.HIGH)
        
        GPIO.setup(channel, GPIO.IN)
        
        while GPIO.input(channel) == GPIO.LOW:
            continue
        
        while GPIO.input(channel) == GPIO.HIGH:
            continue
        
        while j < 40:
            k = 0
            while GPIO.input(channel) == GPIO.LOW:
                continue
           
            while GPIO.input(channel) == GPIO.HIGH:
                k += 1
                if k > 100:
                    break
           
            if k < 8:
                data.append(0)
            else:
                data.append(1)
        
            j += 1
        
        print "sensor is working."
        print data
        
        humidity_bit = data[0:8]
        humidity_point_bit = data[8:16]
        temperature_bit = data[16:24]
        temperature_point_bit = data[24:32]
        check_bit = data[32:40]
        
        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0
        
        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7 - i)
            humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
            temperature += temperature_bit[i] * 2 ** (7 - i)
            temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
            check += check_bit[i] * 2 ** (7 - i)
        
        tmp = humidity + humidity_point + temperature + temperature_point
        
        if check == tmp:
            print "temperature : ", temperature, ", humidity : " , humidity, tmp
            url='http://localhost:5000/control/upload_temperature'
            values ={'time':time.time(),'temperature':temperature,'humidity':humidity}
            headers = {"Content-type":"application/json"}
            jdata = json.dumps(values)
            req = urllib2.Request(url, jdata,headers)
            response = urllib2.urlopen(req)
            print response.read()
    
        else:
            print "wrong"
            print "temperature : ", temperature, ", humidity : " , humidity, " check : ", check, " tmp : ", tmp
    
        GPIO.cleanup()
        time.sleep(stime)

    return true

@app.task
def celery_email(stime):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(21,GPIO.RISING,bouncetime=200)
    while True:
        print 'Monitor and control'
        time.sleep(stime)
    if GPIO.event_detected(21):
        url='http://localhost:5000/control/celery_send_email'
        values ={'status':True}
        headers = {"Content-type":"application/json"}
        jdata = json.dumps(values)
        req = urllib2.Request(url, jdata, headers)
        response = urllib2.urlopen(req)
        return response.read()
    return true