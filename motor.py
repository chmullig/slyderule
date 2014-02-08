import RPi.GPIO as GPIO
import time


class Motor(object):
	def __init__(self, enable_pin, A_1_pin, A_2_pin, B_1_pin, B_2_pin): 
		GPIO.setmode(GPIO.BCM)

		self.enable_pin = enable_pin
		self.coil_A_1_pin = A_1_pin
		self.coil_A_2_pin = A_2_pin
		self.coil_B_1_pin = B_1_pin
		self.coil_B_2_pin = B_2_pin
		
		GPIO.setup(self.enable_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
		GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
 
		GPIO.output(self.enable_pin, 1)

		self.delay = 5/1000.0
 
	def forward(self, steps):	
		for i in range(0, steps):
			self.setStep(1, 0, 1, 0)
			time.sleep(self.delay)
			self.setStep(0, 1, 1, 0)
			time.sleep(self.delay)
			self.setStep(0, 1, 0, 1)
			time.sleep(self.delay)
			self.setStep(1, 0, 0, 1)
			time.sleep(self.delay)
	 
	def backwards(self, steps):	
		for i in range(0, steps):
			self.setStep(1, 0, 0, 1)
			time.sleep(self.delay)
			self.setStep(0, 1, 0, 1)
			time.sleep(self.delay)
			self.setStep(0, 1, 1, 0)
			time.sleep(self.delay)
			self.setStep(1, 0, 1, 0)
			time.sleep(self.delay)

	
	def setStep(self, w1, w2, w3, w4):
		GPIO.output(self.coil_A_1_pin, w1)
		GPIO.output(self.coil_A_2_pin, w2)
		GPIO.output(self.coil_B_1_pin, w3)
		GPIO.output(self.coil_B_2_pin, w4)

	def setDelay(self, delay):
		self.delay = delay/1000.0

	def shutdown(self):
		self.setStep(0, 0, 0, 0)
