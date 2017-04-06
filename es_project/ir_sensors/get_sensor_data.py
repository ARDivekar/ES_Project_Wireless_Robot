import RPi.GPIO as io
motor_pins = {
    'fw_left': 7,
    'fw_right': 23,
    'bw_left': 8,
    'bw_right': 24
}

ir_pins = {
    'l': 18,
    'm': 15,
    'r': 14
}

io.setmode(io.BCM)

for pin_name in ir_pins:
    io.setup(ir_pins[pin_name], io.IN)

def current_ir_sensor_data():
	L = io.input(ir_pins['l'])
	M = io.input(ir_pins['m'])
	R = io.input(ir_pins['r'])
	## The IR sensors by default return 0 when it is triggered
	## (by white/brightness) and 1 when it is not triggered.
	## we want to reverse this.
	L = str(1-int(L))
	M = str(1-int(M))
	R = str(1-int(R))
	return L+M+R	## Will return '101' or whatever
	
