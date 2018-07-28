from random import random

class InputOutputError(Exception):
	pass

config={}
TEST='test'
config[TEST]=False
IN=1
OUT=0
HIGH=1
LOW=0
pins={}
out={}
values={}

def config(path):
    with open(config_name) as config:
    	config = json.load(config)
	if not config[TEST]:
		global RPi
		global GPIO
		import RPi.GPIO as GPIO

def setup(channel,in_out):
	if config[TEST]:
		pins[channel]=in_out
	else:
		GPIO.setup(channel,in_out)

def check_is_input(channel,in_out):
	try:
		if not pins[channel]==in_out:
			raise InputOutputError("Wrong configuration for channel {}! You're treating an input channel as output or vice versa.")
	except KeyError:
		raise InputOutputError("Wrong configuration for channel {}! setup() not called for this channel before calling input() or output().")

def input(channel):
	if config[TEST]:
		check_in_out(channel,IN)
		try:
			values[channel]
		except KeyError:
			return random()
		return values[channel]
	else:
		GPIO.input(channel)

def output(channel,value):
	if config[TEST]:
		check_in_out(channel,OUT)
		out[channel]=value
	else:
		GPIO.output(channel,value)

def set_value(channel,value):
	values[channel]=value

def get_output(channel):
	return out[channel]
	
def cleanup(channel):
	del pins[channel]
	del values[channel]
	del out[channel]

