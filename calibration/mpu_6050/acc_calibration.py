from time import sleep
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU 

n = 50 # No of iteration in each orientation
N = 0 # Total no of iterations
t = 1 # Orientation Duration

sum_product_z = 0
sum_actual_z = 0
sum_squared_z = 0

sum_product_x = 0
sum_actual_x = 0
sum_squared_x = 0

sum_product_y = 0
sum_actual_y = 0
sum_squared_y = 0


print(f"\nLet's start calibration of accelerometer")
sleep(3)


## Get acc and gyro data for positive z
print(f"\nKeep your drone on level surface")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()


for i in range(n):

    ## Summation for Z

    sum_product_z += 1 * MPU.getRawValues().acc_z
    sum_actual_z += MPU.getRawValues().acc_z
    sum_squared_z += 1 ** 2

    ## Summation for X

    sum_product_x += 0 * MPU.getRawValues().acc_x
    sum_actual_x += MPU.getRawValues().acc_x
    sum_squared_x += 0 ** 2

    ## Summation for Y

    sum_product_y += 0 * MPU.getRawValues().acc_y
    sum_actual_y += MPU.getRawValues().acc_y
    sum_squared_y += 0 ** 2

    N += 1
    sleep(t/n)


print(f"\n----------------------------------------------------------------------------")
print(f"\n----------------------------------------------------------------------------")




## Get acc and gyro data for negative x
print(f"\nKeep your drone on right side")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()


for i in range(n):

    ## Summation for Z

    sum_product_z += 0 * MPU.getRawValues().acc_z
    sum_actual_z += MPU.getRawValues().acc_z
    sum_squared_z += 0 ** 2

    ## Summation for X

    sum_product_x += -1 * MPU.getRawValues().acc_x
    sum_actual_x += MPU.getRawValues().acc_x
    sum_squared_x += 1 ** 2

    ## Summation for Y

    sum_product_y += 0 * MPU.getRawValues().acc_y
    sum_actual_y += MPU.getRawValues().acc_y
    sum_squared_y += 0 ** 2

    N += 1

    sleep(t/n)


print(f"\n----------------------------------------------------------------------------")
print(f"\n----------------------------------------------------------------------------")



## Get acc and gyro data for positive x
print(f"\nKeep your drone on left side")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()


for i in range(n):

    ## Summation for Z

    sum_product_z += 0 * MPU.getRawValues().acc_z
    sum_actual_z += MPU.getRawValues().acc_z
    sum_squared_z += 0 ** 2

    ## Summation for X

    sum_product_x += 1 * MPU.getRawValues().acc_x
    sum_actual_x += MPU.getRawValues().acc_x
    sum_squared_x += 1 ** 2

    ## Summation for Y

    sum_product_y += 0 * MPU.getRawValues().acc_y
    sum_actual_y += MPU.getRawValues().acc_y
    sum_squared_y += 0 ** 2

    N += 1

    sleep(t/n)


print(f"\n----------------------------------------------------------------------------")
print(f"\n----------------------------------------------------------------------------")




## Get acc and gyro data for negative y
print(f"\nKeep your drone nose down")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()


for i in range(n):

    ## Summation for Z

    sum_product_z += 0 * MPU.getRawValues().acc_z
    sum_actual_z += MPU.getRawValues().acc_z
    sum_squared_z += 0 ** 2

    ## Summation for X

    sum_product_x += 0 * MPU.getRawValues().acc_x
    sum_actual_x += MPU.getRawValues().acc_x
    sum_squared_x += 0 ** 2

    ## Summation for Y

    sum_product_y += -1 * MPU.getRawValues().acc_y
    sum_actual_y += MPU.getRawValues().acc_y
    sum_squared_y += 1 ** 2

    N += 1

    sleep(t/n)


print(f"\n----------------------------------------------------------------------------")
print(f"\n----------------------------------------------------------------------------")




## Get acc and gyro data for positive y
print(f"\nKeep your drone nose up")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()


for i in range(n):
    ## Summation for Z

    sum_product_z += 0 * MPU.getRawValues().acc_z
    sum_actual_z += MPU.getRawValues().acc_z
    sum_squared_z += 0 ** 2

    ## Summation for X

    sum_product_x += 0 * MPU.getRawValues().acc_x
    sum_actual_x += MPU.getRawValues().acc_x
    sum_squared_x += 0 ** 2

    ## Summation for Y

    sum_product_y += 1 * MPU.getRawValues().acc_y
    sum_actual_y += MPU.getRawValues().acc_y
    sum_squared_y += 1 ** 2

    N += 1

    sleep(t/n)


print(f"\n----------------------------------------------------------------------------")
print(f"\n----------------------------------------------------------------------------")




## Get acc and gyro data for negative z
print(f"\nKeep your drone on its back")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    ## Summation for Z

    sum_product_z += -1 * MPU.getRawValues().acc_z
    sum_actual_z += MPU.getRawValues().acc_z
    sum_squared_z += 1 ** 2

    ## Summation for X

    sum_product_x += 0 * MPU.getRawValues().acc_x
    sum_actual_x += MPU.getRawValues().acc_x
    sum_squared_x += 0 ** 2

    ## Summation for Y

    sum_product_y += 0 * MPU.getRawValues().acc_y
    sum_actual_y += MPU.getRawValues().acc_y
    sum_squared_y += 0 ** 2
    N += 1

    sleep(t/n)


print(f"\n----------------------------------------------------------------------------")
print(f"\n----------------------------------------------------------------------------")


acc_z_multiplier = sum_product_z / sum_squared_z
acc_z_offset =  sum_actual_z / N

acc_x_multiplier = sum_product_x / sum_squared_x
acc_x_offset =  sum_actual_x / N

acc_y_multiplier = sum_product_y / sum_squared_y
acc_y_offset =  sum_actual_y / N

print("N = " + str(N))
 
print("acc_x_multiplier = " + str(acc_x_multiplier))
print("acc_y_multiplier = " + str(acc_y_multiplier))
print("acc_z_multiplier = " + str(acc_z_multiplier))

print("acc_x_offset = " + str(acc_x_offset))
print("acc_y_offset = " + str(acc_y_offset))
print("acc_z_offset = " + str(acc_z_offset))

