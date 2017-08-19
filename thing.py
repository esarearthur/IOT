import RPi.GPIO as GPIO

LEDPIN = 23
SWITCHPIN = 24

class Thing(object):
	def __init__(self):
		super(Thing, self).__init__()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(LEDPIN, GPIO.OUT, initial=GPIO.LOW)

	def read_switch(self):
		"""Read the switch state and return its current value."""
		return GPIO.input(SWITCHPIN)

	def set_led(self, value):
		"""Set the LED to the provided value (True = on, False = off)."""
		GPIO.output(LEDPIN, value)
		
