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

def LookForSpot():
	ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
	frontWheels.turn_straight()
	found = False
	start = False
	obstacleEnd = False
	timer = 0
	time.sleep(1)
	while (found == False):
		backWheels.forward()
		backWheels.speed = forward_speed
		distance = ua.get_distance()
		if (distance < 20):
			start = True
		if (start == True):
			print "Obstacle"
			time.sleep(0.2)
			distance = ua.get_distance()
			if (distance > 20):
				obstacleEnd = True
				
			while (obstacleEnd == True):
				print "Empty Space"
				time.sleep(0.1)
				distance = ua.get_distance()
				timer += 1
				if (distance < 50):
					obstacleEnd = False
					print "New Obstacle"
				print "Distance %scm" % distance
		if (timer > 7):
			found = True
		else:
			start = False
			continue
	backWheels.stop()
	print "SPOT FOUND"
	time.sleep(1)
	print "CREEPING FORWARD"
	backWheels.forward()
	backWheels.speed = forward_speed
	time.sleep(0.4)
	print "READY TO PARK"
	backWheels.stop()
	ParktheBatmobile()

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
	time.sleep(1.1)
	backWheels.stop()
	
	time.sleep(1)
	
	frontWheels.turn_straight()
	backWheels.forward()
	backWheels.speed = forward_speed
	time.sleep(0.4)
	backWheels.stop()	
	


if __name__ == '__main__':
	try:
		LookForSpot()
	except KeyboardInterrupt:
		backWheels.stop()
