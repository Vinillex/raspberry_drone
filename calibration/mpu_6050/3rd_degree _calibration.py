from time import sleep
import numpy as np 
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU 

n = 50 # No of iteration in each orientation
N = 0 # Total no of iterations
t = 1 # Orientation Duration


## For Z direction
z_o_1 = 0  #y
z_o_2 = 0  #xy
z_o_3 = 0  #x2y
z_o_4 = 0  #x3y

z_6 = 0  #x6
z_5 = 0  #x5
z_4 = 0  #x4
z_3 = 0  #x3
z_2 = 0  #x2
z_1 = 0  #x

## For x direction
x_o_1 = 0  #y
x_o_2 = 0  #xy
x_o_3 = 0  #x2y
x_o_4 = 0  #x3y

x_6 = 0  #x6
x_5 = 0  #x5
x_4 = 0  #x4
x_3 = 0  #x3
x_2 = 0  #x2
x_1 = 0  #x

## For Y direction
y_o_1 = 0  #y
y_o_2 = 0  #xy
y_o_3 = 0  #x2y
y_o_4 = 0  #x3y

y_6 = 0  #x6
y_5 = 0  #x5
y_4 = 0  #x4
y_3 = 0  #x3
y_2 = 0  #x2
y_1 = 0  #x

print(f"\nLet's start calibration of accelerometer")
sleep(3)


## Get acc and gyro data for positive z
print(f"\nKeep your drone on level surface")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    #Z direction
    z = MPU.getRawValues().acc_z
    z_offset = 1 - z

    z_o_1 += z_offset
    z_o_2 += z_offset * z
    z_o_3 += z_offset * z ** 2
    z_o_4 += z_offset * z ** 3

    z_6 += z ** 6
    z_5 += z ** 5
    z_4 += z ** 4
    z_3 += z ** 3
    z_2 += z ** 2
    z_1 += z
    #X direction
    x = MPU.getRawValues().acc_x
    x_offset = 0 - x

    x_o_1 += x_offset
    x_o_2 += x_offset * x
    x_o_3 += x_offset * x ** 2
    x_o_4 += x_offset * x ** 3
    x_6 += x ** 6
    x_5 += x ** 5
    x_4 += x ** 4
    x_3 += x ** 3
    x_2 += x ** 2
    x_1 += x

    #Y direction
    y = MPU.getRawValues().acc_y
    y_offset = 0 - y

    y_o_1 += y_offset
    y_o_2 += y_offset * y
    y_o_3 += y_offset * y ** 2
    y_o_4 += y_offset * y ** 3

    y_6 += y ** 6
    y_5 += y ** 5
    y_4 += y ** 4
    y_3 += y ** 3
    y_2 += y ** 2
    y_1 += y

    N += 1
    sleep(t/n)

## Get acc and gyro data for negative x
print(f"\nKeep your drone on right surface")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    #Z direction
    z = MPU.getRawValues().acc_z
    z_offset = 0 - z

    z_o_1 += z_offset
    z_o_2 += z_offset * z
    z_o_3 += z_offset * z ** 2
    z_o_4 += z_offset * z ** 3

    z_6 += z ** 6
    z_5 += z ** 5
    z_4 += z ** 4
    z_3 += z ** 3
    z_2 += z ** 2
    z_1 += z

    #X direction
    x = MPU.getRawValues().acc_x
    x_offset = -1 - x

    x_o_1 += x_offset
    x_o_2 += x_offset * x
    x_o_3 += x_offset * x ** 2
    x_o_4 += x_offset * x ** 3
    x_6 += x ** 6
    x_5 += x ** 5
    x_4 += x ** 4
    x_3 += x ** 3
    x_2 += x ** 2
    x_1 += x

    #Y direction
    y = MPU.getRawValues().acc_y
    y_offset = 0 - y

    y_o_1 += y_offset
    y_o_2 += y_offset * y
    y_o_3 += y_offset * y ** 2
    y_o_4 += y_offset * y ** 3

    y_6 += y ** 6
    y_5 += y ** 5
    y_4 += y ** 4
    y_3 += y ** 3
    y_2 += y ** 2
    y_1 += y

    N += 1
    sleep(t/n)

## Get acc and gyro data for positive x
print(f"\nKeep your drone on left surface")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    #Z direction
    z = MPU.getRawValues().acc_z
    z_offset = 0 - z

    z_o_1 += z_offset
    z_o_2 += z_offset * z
    z_o_3 += z_offset * z ** 2
    z_o_4 += z_offset * z ** 3

    z_6 += z ** 6
    z_5 += z ** 5
    z_4 += z ** 4
    z_3 += z ** 3
    z_2 += z ** 2
    z_1 += z

    #X direction
    x = MPU.getRawValues().acc_x
    x_offset = 1 - x

    x_o_1 += x_offset
    x_o_2 += x_offset * x
    x_o_3 += x_offset * x ** 2
    x_o_4 += x_offset * x ** 3
    x_6 += x ** 6
    x_5 += x ** 5
    x_4 += x ** 4
    x_3 += x ** 3
    x_2 += x ** 2
    x_1 += x

    #Y direction
    y = MPU.getRawValues().acc_y
    y_offset = 0 - y

    y_o_1 += y_offset
    y_o_2 += y_offset * y
    y_o_3 += y_offset * y ** 2
    y_o_4 += y_offset * y ** 3

    y_6 += y ** 6
    y_5 += y ** 5
    y_4 += y ** 4
    y_3 += y ** 3
    y_2 += y ** 2
    y_1 += y

    N += 1
    sleep(t/n)

## Get acc and gyro data for negative y
print(f"\nKeep your drone nose down")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    #Z direction
    z = MPU.getRawValues().acc_z
    z_offset = 0 - z

    z_o_1 += z_offset
    z_o_2 += z_offset * z
    z_o_3 += z_offset * z ** 2
    z_o_4 += z_offset * z ** 3

    z_6 += z ** 6
    z_5 += z ** 5
    z_4 += z ** 4
    z_3 += z ** 3
    z_2 += z ** 2
    z_1 += z
    #X direction
    x = MPU.getRawValues().acc_x
    x_offset = 0 - x

    x_o_1 += x_offset
    x_o_2 += x_offset * x
    x_o_3 += x_offset * x ** 2
    x_o_4 += x_offset * x ** 3
    x_6 += x ** 6
    x_5 += x ** 5
    x_4 += x ** 4
    x_3 += x ** 3
    x_2 += x ** 2
    x_1 += x

    #Y direction
    y = MPU.getRawValues().acc_y
    y_offset = -1 - y

    y_o_1 += y_offset
    y_o_2 += y_offset * y
    y_o_3 += y_offset * y ** 2
    y_o_4 += y_offset * y ** 3

    y_6 += y ** 6
    y_5 += y ** 5
    y_4 += y ** 4
    y_3 += y ** 3
    y_2 += y ** 2
    y_1 += y

    N += 1
    sleep(t/n)

## Get acc and gyro data for positive y
print(f"\nKeep your drone nose up")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    #Z direction
    z = MPU.getRawValues().acc_z
    z_offset = 0 - z

    z_o_1 += z_offset
    z_o_2 += z_offset * z
    z_o_3 += z_offset * z ** 2
    z_o_4 += z_offset * z ** 3

    z_6 += z ** 6
    z_5 += z ** 5
    z_4 += z ** 4
    z_3 += z ** 3
    z_2 += z ** 2
    z_1 += z

    #X direction
    x = MPU.getRawValues().acc_x
    x_offset = 0 - x

    x_o_1 += x_offset
    x_o_2 += x_offset * x
    x_o_3 += x_offset * x ** 2
    x_o_4 += x_offset * x ** 3
    x_6 += x ** 6
    x_5 += x ** 5
    x_4 += x ** 4
    x_3 += x ** 3
    x_2 += x ** 2
    x_1 += x

    #Y direction
    y = MPU.getRawValues().acc_y
    y_offset = 1 - y

    y_o_1 += y_offset
    y_o_2 += y_offset * y
    y_o_3 += y_offset * y ** 2
    y_o_4 += y_offset * y ** 3

    y_6 += y ** 6
    y_5 += y ** 5
    y_4 += y ** 4
    y_3 += y ** 3
    y_2 += y ** 2
    y_1 += y

    N += 1
    sleep(t/n)

## Get acc and gyro data for negative z
print(f"\nKeep your drone on its back")
var = input(f'\nTo register the value, press "Y" and any other key to stop calibration: ')
if var.lower() != "y":
    print(f"\nCalibration Ended")
    exit()

for i in range(n):

    #Z direction
    z = MPU.getRawValues().acc_z
    z_offset = -1 - z

    z_o_1 += z_offset
    z_o_2 += z_offset * z
    z_o_3 += z_offset * z ** 2
    z_o_4 += z_offset * z ** 3

    z_6 += z ** 6
    z_5 += z ** 5
    z_4 += z ** 4
    z_3 += z ** 3
    z_2 += z ** 2
    z_1 += z

    #X direction
    x = MPU.getRawValues().acc_x
    x_offset = 0 - x

    x_o_1 += x_offset
    x_o_2 += x_offset * x
    x_o_3 += x_offset * x ** 2
    x_o_4 += x_offset * x ** 3
    x_6 += x ** 6
    x_5 += x ** 5
    x_4 += x ** 4
    x_3 += x ** 3
    x_2 += x ** 2
    x_1 += x

    #Y direction
    y = MPU.getRawValues().acc_y
    y_offset = 0 - y

    y_o_1 += y_offset
    y_o_2 += y_offset * y
    y_o_3 += y_offset * y ** 2
    y_o_4 += y_offset * y ** 3

    y_6 += y ** 6
    y_5 += y ** 5
    y_4 += y ** 4
    y_3 += y ** 3
    y_2 += y ** 2
    y_1 += y

    N += 1
    sleep(t/n)



ZA = np.array([
    [z_3, z_2, z_1, N], 
    [z_4, z_3, z_2, N * z_1], 
    [z_5, z_4, z_3, N * z_2],
    [z_6, z_5, z_4, N * z_3],
    ]) 

ZB = np.array([
    z_o_1, 
    z_o_2, 
    z_o_3, 
    z_o_4])

z_list = np.linalg.solve(ZA, ZB)

XA = np.array([
    [x_3, x_2, x_1, N], 
    [x_4, x_3, x_2, N * x_1], 
    [x_5, x_4, x_3, N * x_2],
    [x_6, x_5, x_4, N * x_3],
    ]) 

XB = np.array([
    x_o_1, 
    x_o_2, 
    x_o_3, 
    x_o_4])

x_list = np.linalg.solve(XA, XB)

YA = np.array([
    [y_3, y_2, y_1, N], 
    [y_4, y_3, y_2, N * y_1], 
    [y_5, y_4, y_3, N * y_2],
    [y_6, y_5, y_4, N * y_3],
    ]) 

YB = np.array([
    y_o_1, 
    y_o_2, 
    y_o_3, 
    y_o_4])

y_list = np.linalg.solve(YA, YB)

a_z = z_list[0]
b_z = z_list[1]
c_z = z_list[2]
d_z = z_list[3]

a_x = x_list[0]
b_x = x_list[1]
c_x = x_list[2]
d_x = x_list[3]

a_y = y_list[0]
b_y = y_list[1]
c_y = y_list[2]
d_y = y_list[3]

print("a_z = " + str(a_z))
print("b_z = " + str(b_z))
print("c_z = " + str(c_z))
print("d_z = " + str(d_z))
print("a_x = " + str(a_x))
print("b_x = " + str(b_x))
print("c_x = " + str(c_x))
print("d_x = " + str(d_x))
print("a_y = " + str(a_y))
print("b_y = " + str(b_y))
print("c_y = " + str(c_y))
print("d_y = " + str(d_y))