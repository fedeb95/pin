from random import random

class InputOutputError(Exception):
	pass

config={}
pins={}
out={}
values={}
IN=0
OUT=1

def setup(channel,in_out):
	pins[channel]=in_out

def check_is_input(channel,in_out):
	try:
		if not pins[channel]==in_out:
			raise InputOutputError("Wrong configuration for channel {}! You're treating an input channel as output or vice versa.")
	except KeyError:
		raise InputOutputError("Wrong configuration for channel {}! setup() not called for this channel before calling input() or output().")

def input(channel):
	check_in_out(channel,IN)
	try:
		values[channel]
	except KeyError:
		return random()
	return values[channel]

def output(channel,value):
	check_in_out(channel,OUT)
	out[channel]=value

def set_value(channel,value):
	values[channel]=value

def get_output(channel):
	return out[channel]
	
	

