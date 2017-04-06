import RPi.GPIO as io
from config import motor_pins as mpins
from config import ir_pins as ipins
from util import *
from time import sleep

def init():
	io.setmode(io.BCM)
	out_pins(mpins['fw_left'], mpins['fw_right'], mpins['back_left'], mpins['back_right'])


def stop():
        print("stop")
        low_pins(mpins['fw_left'], mpins['back_left'], mpins['back_right'], mpins['fw_right'])


def forward():
	print("forward")
	high_pins(mpins['fw_left'], mpins['fw_right'])
	low_pins(mpins['back_left'], mpins['back_right'])
	
def go_forward():
	forward()
	sleep(2.5)
	stop()


def backward():
        print("backward")
	high_pins(mpins['back_left'], mpins['back_right'])
	low_pins(mpins['fw_left'], mpins['fw_right'])
	
def go_backward():
        backward()
        sleep(2.5)
        stop()


def right():
        print("right")
	high_pins(mpins['fw_left'], mpins['back_right'])
	low_pins(mpins['back_left'], mpins['fw_right'])
	

def left():
        print("left")
	high_pins(mpins['fw_right'], mpins['back_left'])
	low_pins(mpins['fw_left'], mpins['back_right'])


def turnaround(direction="left"):
	if direction == "left":
		print("Doing a 180, anticlockwise")
		left()
	else:
		print("Doing a 180, clockwise")
                right()	
	sleep(1)
	stop()

def turn_90_right():
	right()
	sleep(0.55)
	stop()

def turn_45_right():
        right()
        sleep(0.3)
        stop()

def turn_90_left():
        left()
        sleep(0.55)
        stop()

def turn_45_left():
        left()
        sleep(0.3)
        stop()


def burnout(direction="left"):
        if direction == "left":
                print("Doing a 180, anticlockwise")
                left()
        else:
                print("Doing a 180, clockwise")
                right()
        sleep(5)
        stop()
	

init()
