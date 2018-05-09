from picar import front_wheels
from picar import back_wheels
import time
import picar

picar.setup()

frontWheels = front_wheels.Front_Wheels(db='config')
backWheels = back_wheels.Back_Wheels(db='config')
frontWheels.turning_max = 45

