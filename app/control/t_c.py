from __future__ import absolute_import
from celery import Celery
from mgpio import *



app = Celery(__name__,include=['app.control.views'], broker='redis://localhost:6379/0')

@app.task
def mygpio_task(pin_id,status):
    gpio_change(int(pin_id), status)


@app.task
def get_temp()
	upload_temperature()
