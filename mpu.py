from mpu6050 import mpu6050
from inv import INV
import time


mpu = mpu6050(0x68)
acc_x_multiplier = 0.9898339843749999
acc_y_multiplier = 0.9995483398437499
acc_z_multiplier = 1.00903076171875
acc_x_offset = -0.005328776041666691
acc_y_offset = -0.027025146484374967
acc_z_offset = -0.06608642578124997
gyr_x_offset = 1.4427480916030535
gyr_y_offset = -0.7709923664122138
gyr_z_offset = 1.1412213740458017

class MPU:

    def __init__(self) -> None:
        pass

    def getRawValues():
        accRaw = mpu.get_accel_data(g=True)
        gyrRaw = mpu.get_gyro_data()
        inv = INV(
        acc_x = accRaw['x'],
        acc_y = accRaw['y'],
        acc_z = accRaw['z'],
        gyr_x = gyrRaw['x'],
        gyr_y = gyrRaw['y'],
        gyr_z = gyrRaw['z'],
        )
        return inv
    
    def getCalibratedValues():
        accRaw = mpu.get_accel_data(g=True)
        gyrRaw = mpu.get_gyro_data()
        inv = INV(
        acc_x = (accRaw['x'] * acc_x_multiplier) + acc_x_offset,
        acc_y = (accRaw['y'] * acc_y_multiplier) + acc_y_offset,
        acc_z = (accRaw['z'] * acc_z_multiplier) + acc_z_offset,
        #Gyroscope data is not callibrated as it's more precise and doesn't drift much
        gyr_x = gyrRaw['x'] + gyr_x_offset,
        gyr_y = gyrRaw['y'] + gyr_y_offset,
        gyr_z = gyrRaw['z'] + gyr_z_offset,
        )
        return inv
