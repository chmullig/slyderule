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
		setStep(0, 0, 0, 0)
 
motor1 = Motor(18, 4, 17, 23, 24)
motor2 = Motor(18, 22, 27, 18, 25)

while True:
	delay = raw_input("Delay between steps (milliseconds, or -1 to quit)? ")
	if delay == "-1":
		break
	motor1.setDelay(int(delay))
	motor1.setDelay(int(delay))
	steps = raw_input("How many steps forward? ")
	motor1.forward(int(steps))
	motor2.forward(int(steps))
	steps = raw_input("How many steps backwards? ")
	motor1.backwards(int(steps))
	motor2.backwards(int(steps))

motor1.shutdown()
motor2.shutdown()
