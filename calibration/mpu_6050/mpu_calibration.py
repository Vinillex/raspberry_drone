from time import sleep
import sys
import os


current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU 
# Add the parent directory of script1.py to the sys.path
g = 9.81

print(f"\nLet's start calibration of accelerometer")
sleep(3)


## Get acc and gyro data for positive z
print(f"\nKeep your drone on level surface")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()
acc_z_p = MPU.getRawValues().acc_z
gyr_z_p = MPU.getRawValues().gyr_z
print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Z direction at level surface is {acc_z_p}")
print(f"\nGyro Value in Z direction at level surface is {gyr_z_p}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for negative x
print(f"\nKeep your drone on right side")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()
acc_x_n = MPU.getRawValues().acc_x
gyr_x_n = MPU.getRawValues().gyr_x
print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in X direction when on right side is {acc_x_n}")
print(f"\nGyro Value in X direction when on right side is {gyr_x_n}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")



## Get acc and gyro data for positive x
print(f"\nKeep your drone on left side")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()
acc_x_p = MPU.getRawValues().acc_x
gyr_x_p = MPU.getRawValues().gyr_x
print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in X direction when on left side is {acc_x_p}")
print(f"\nGyro Value in X direction when on left side is {gyr_x_p}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for negative y
print(f"\nKeep your drone nose down")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()
acc_y_n = MPU.getRawValues().acc_y
gyr_y_n = MPU.getRawValues().gyr_y
print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Y direction when nose down is {acc_y_n}")
print(f"\nGyro Value in Y direction when nose down is {gyr_y_n}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for positive y
print(f"\nKeep your drone nose up")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()
acc_y_p = MPU.getRawValues().acc_y
gyr_y_p = MPU.getRawValues().gyr_y
print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Y direction when nose up is {acc_y_p}")
print(f"\nGyro Value in Y direction when nose up is {gyr_y_p}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for negative z
print(f"\nKeep your drone on its back")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()
acc_z_n = MPU.getRawValues().acc_z
gyr_z_n = MPU.getRawValues().gyr_z
print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Z direction on its back is {acc_z_n}")
print(f"\nGyro Value in Z direction on its back is {gyr_z_n}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")


##Accelerometer Calculation
acc_x_range = acc_x_p - acc_x_n
acc_y_range = acc_y_p - acc_y_n
acc_z_range = acc_z_p - acc_z_n

acc_x_multiplier = acc_x_range / (2 * g)
acc_y_multiplier = acc_y_range / (2 * g)
acc_z_multiplier = acc_z_range / (2 * g)

acc_x_offset = g - (acc_x_p * acc_x_multiplier)
acc_y_offset = g - (acc_y_p * acc_y_multiplier)
acc_z_offset = g - (acc_z_p * acc_z_multiplier)

##Gyroscope Calculation

gyr_x_avg = (gyr_x_p + gyr_x_n)/2
gyr_y_avg = (gyr_y_p + gyr_y_n)/2
gyr_z_avg = (gyr_z_p + gyr_z_n)/2

gyr_x_offset = -gyr_x_avg
gyr_y_offset = -gyr_y_avg
gyr_z_offset = -gyr_z_avg


print("acc_x_multiplier = " + str(acc_x_multiplier))
print("acc_y_multiplier = " + str(acc_y_multiplier))
print("acc_z_multiplier = " + str(acc_z_multiplier))

print("acc_x_offset = " + str(acc_x_offset))
print("acc_y_offset = " + str(acc_y_offset))
print("acc_z_offset = " + str(acc_z_offset))

print("gyr_x_offset = " + str(gyr_x_offset))
print("gyr_y_offset = " + str(gyr_y_offset))
print("gyr_z_offset = " + str(gyr_z_offset))

