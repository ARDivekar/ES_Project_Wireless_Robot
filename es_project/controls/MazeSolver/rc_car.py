import RPi.GPIO as io
from config import motor_pins as mpins

def init():
    io.cleanup()
    io.setmode(io.BCM)
    for k, v in mpins.items():
        io.setup(v, io.OUT)

def forward():
    io.output(mpins['fw_left'], True)
    io.output(mpins['fw_right'], True)
    io.output(mpins['bw_left'], False)
    io.output(mpins['bw_right'], False)

def backward():
    io.output(mpins['bw_left'], True)
    io.output(mpins['bw_right'], True)
    io.output(mpins['fw_left'], False)
    io.output(mpins['fw_right'], False)

def stop():
    io.output(mpins['bw_left'], False)
    io.output(mpins['bw_right'], False)
    io.output(mpins['fw_left'], False)
    io.output(mpins['fw_right'], False)

def left():
    io.output(mpins['bw_left'], True)
    io.output(mpins['fw_right'], True)
    io.output(mpins['fw_left'], False)
    io.output(mpins['bw_right'], False)

def right():
    io.output(mpins['fw_left'], True)
    io.output(mpins['bw_right'], True)
    io.output(mpins['bw_left'], False)
    io.output(mpins['fw_right'], False)

init()
