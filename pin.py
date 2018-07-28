from random import random
import json

class InputOutputError(Exception):
    pass

conf={}
TEST='test'
conf[TEST]=False
IN=1
OUT=0
HIGH=1
LOW=0
BCM=0
BOARD=1
pins={}
out={}
values={}

def config(path):
    with open(path) as c:
        conf = json.load(c)
    if not conf[TEST]:
        global RPi
        global GPIO
        import RPi.GPIO as GPIO

def setup(channel,in_out):
    global conf
    if conf[TEST]:
        pins[channel]=in_out
    else:
        if in_out == IN:
            GPIO.setup(channel,GPIO.IN)
        else:
            GPIO.setup(chanel,GPIO.OUT)

def check_in_out(channel,in_out):
    try:
        if not pins[channel]==in_out:
            raise InputOutputError("Wrong confuration for channel {}! You're treating an input channel as output or vice versa.")
    except KeyError:
        raise InputOutputError("Wrong confuration for channel {}! setup() not called for this channel before calling input() or output().")

def setmode(mode):
    if conf[TEST]:
        pass
    else:
        if mode == BCM:
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)
        

def input(channel):
    if conf[TEST]:
        check_in_out(channel,IN)
        try:
            values[channel]
        except KeyError:
            return random()
        return values[channel]
    else:
        GPIO.input(channel)

def output(channel,value):
    if conf[TEST]:
        check_in_out(channel,OUT)
        out[channel]=value
    else:
        GPIO.output(channel,value)

def set_value(channel,value):
    values[channel]=value

def get_output(channel):
    return out[channel]
    
def cleanup(channel):
    if pins[channel]==IN:
        del values[channel]
    else:
        del out[channel]
    del pins[channel]
