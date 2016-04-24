import time, threading

import RPi.GPIO as GPIO
import urllib
import urllib2
import json

def upload_temperature():
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
	
		else:
		    print "wrong"
		    print "temperature : ", temperature, ", humidity : " , humidity, " check : ", check, " tmp : ", tmp
	
		url='http://localhost/control/upload_temperature'
    	values ={'time':time.time(),'temperature':temperature,'humidity':humidity}
	
    	jdata = json.dumps(values)
    	req = urllib2.Request(url, jdata)
    	response = urllib2.urlopen(req)
    	return response.read()
    	time.sleep(20)