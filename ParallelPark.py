from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar

picar.setup()

frontWheels = front_wheels.Front_Wheels(db='config')
backWheels = back_wheels.Back_Wheels(db='config')
frontWheels.turning_max = 45

forward_speed = 45
backward_speed = 45

def ParktheBatmobile():
	finished = False
	timer = 0


	ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
	frontWheels.turn_left()
	frontWheels.turn_straight()	

	
	
	distance = ua.get_distance()
	print "distance: %scm" % distance

	backWheels.backward()
	time.sleep(0.5)
	
	frontWheels.turn_right()
	backWheels.backward()
	backWheels.speed = backward_speed
	
	time.sleep(1.15)
	frontWheels.turn_left()
	time.sleep(1.20)
	backWheels.stop()
	
	time.sleep(1)
	
	frontWheels.turn_straight()
	backWheels.forward()
	backWheels.speed = forward_speed
	time.sleep(0.5)
	backWheels.stop()	
	


if __name__ == '__main__':
	try:
		ParktheBatmobile()
	except KeyboardInterrupt:
		backWheels.stop()
