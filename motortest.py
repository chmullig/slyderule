from motor import Motor

motor1 = Motor(18, 4, 17, 23, 24)
motor2 = Motor(18, 22, 27, 18, 25)

if __name__ == "__main__":
	while True:
		delay = raw_input("Delay between steps (milliseconds, or -1 to quit)? ")
		if delay == "-1":
			break
		motor1.setDelay(int(delay))
		motor2.setDelay(int(delay))
		steps = raw_input("How many steps forward? ")
		motor1.forward(int(steps))
		motor2.forward(int(steps))
		motor1.backwards(int(steps))
		motor2.backwards(int(steps))

	motor1.shutdown()
	motor2.shutdown()
