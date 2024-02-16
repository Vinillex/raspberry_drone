from time import sleep
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU 

n = 50 #No of iteration in each orientation
t = 1 #Orientation Duration


print(f"\nLet's start calibration of accelerometer")
sleep(3)


## Get acc and gyro data for positive z
print(f"\nKeep your drone on level surface")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

acc_z_p = 0
acc_x_z_p = 0
acc_y_z_p = 0

for i in range(n):
    acc_z_p = acc_z_p + MPU.getRawValues().acc_z

    acc_x_z_p = acc_x_z_p + MPU.getRawValues().acc_x
    acc_y_z_p = acc_y_z_p + MPU.getRawValues().acc_y
    sleep(t/n)

acc_z_p = acc_z_p / n

acc_x_z_p = acc_x_z_p / n
acc_y_z_p = acc_y_z_p/n

print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Z direction at level surface is {acc_z_p}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for negative x
print(f"\nKeep your drone on right side")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

acc_x_n = 0

acc_z_x_n = 0
acc_y_x_n = 0

for i in range(n):
    acc_x_n = acc_x_n + MPU.getRawValues().acc_x

    acc_z_x_n = acc_z_x_n + MPU.getRawValues().acc_z
    acc_y_x_n = acc_y_x_n + MPU.getRawValues().acc_y
    sleep(t/n)

acc_x_n = acc_x_n / n

acc_z_x_n = acc_z_x_n / n
acc_y_x_n = acc_y_x_n / n

print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in X direction when on right side is {acc_x_n}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")



## Get acc and gyro data for positive x
print(f"\nKeep your drone on left side")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

acc_x_p = 0

acc_z_x_p = 0
acc_y_x_p = 0

for i in range(n):
    acc_x_p = acc_x_p + MPU.getRawValues().acc_x

    acc_z_x_p = acc_z_x_p + MPU.getRawValues().acc_z
    acc_y_x_p = acc_y_x_p + MPU.getRawValues().acc_y
    sleep(t/n)

acc_x_p = acc_x_p / n

acc_z_x_p = acc_z_x_p / n
acc_y_x_p = acc_y_x_p / n

print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in X direction when on left side is {acc_x_p}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for negative y
print(f"\nKeep your drone nose down")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

acc_y_n = 0

acc_z_y_n = 0
acc_x_y_n = 0

for i in range(n):
    acc_y_n = acc_y_n + MPU.getRawValues().acc_y

    acc_z_y_n = acc_z_y_n + MPU.getRawValues().acc_z
    acc_x_y_n  = acc_x_y_n  + MPU.getRawValues().acc_x
    sleep(t/n)

acc_y_n = acc_y_n / n

acc_z_y_n = acc_z_y_n / n
acc_x_y_n = acc_x_y_n / n

print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Y direction when nose down is {acc_y_n}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for positive y
print(f"\nKeep your drone nose up")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()


acc_y_p = 0

acc_z_y_p = 0
acc_x_y_p = 0

for i in range(n):
    acc_y_p = acc_y_p + MPU.getRawValues().acc_y

    acc_z_y_p = acc_z_y_p + MPU.getRawValues().acc_z
    acc_x_y_p  = acc_x_y_p  + MPU.getRawValues().acc_x
    sleep(t/n)

acc_y_p = acc_y_p / n

acc_z_y_p = acc_z_y_p / n
acc_x_y_p = acc_x_y_p / n

print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Y direction when nose up is {acc_y_p}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")




## Get acc and gyro data for negative z
print(f"\nKeep your drone on its back")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

acc_z_n = 0
acc_x_z_n = 0
acc_y_z_n = 0

for i in range(n):
    acc_z_n = acc_z_n + MPU.getRawValues().acc_z

    acc_x_z_n = acc_x_z_n + MPU.getRawValues().acc_x
    acc_y_z_n = acc_y_z_n + MPU.getRawValues().acc_y
    sleep(t/n)

acc_z_n = acc_z_n/n

acc_x_z_n = acc_x_z_n/n
acc_y_z_n = acc_y_z_n/n

print(f"\n----------------------------------------------------------------------------")
print(f"\nAcceleration in Z direction on its back is {acc_z_n}")
print(f"\n----------------------------------------------------------------------------")
print(f"----------------------------------------------------------------------------")


# Calculation for z axis
sum_actual_z = acc_z_n + acc_z_p + ((acc_y_z_n + acc_x_z_n + acc_y_z_p + acc_x_z_p)  / 4)
sum_product_z = -acc_z_n + acc_z_p

acc_z_multiplier = sum_product_z / 2
acc_z_offset = sum_actual_z / 3

#Calculation for y axis
sum_actual_y = acc_y_n + acc_y_p + ((acc_z_y_n + acc_x_y_n + acc_z_y_p + acc_x_y_p)  / 4)
sum_product_y = -acc_y_n + acc_y_p

acc_y_multiplier = sum_product_y / 2
acc_y_offset = sum_actual_y / 3

#Calculation for x axis
sum_actual_x = acc_x_n + acc_x_p + ((acc_z_x_n + acc_y_x_n + acc_z_x_p + acc_y_x_p)  / 4)
sum_product_x = -acc_x_n + acc_x_p

acc_x_multiplier = sum_product_x / 2
acc_x_offset = sum_actual_x / 3

 
print("acc_x_multiplier = " + str(acc_x_multiplier))
print("acc_y_multiplier = " + str(acc_y_multiplier))
print("acc_z_multiplier = " + str(acc_z_multiplier))

print("acc_x_offset = " + str(acc_x_offset))
print("acc_y_offset = " + str(acc_y_offset))
print("acc_z_offset = " + str(acc_z_offset))


#print("gyr_x_offset = " + str(gyr_x_offset))
#print("gyr_y_offset = " + str(gyr_y_offset))
#print("gyr_z_offset = " + str(gyr_z_offset))

