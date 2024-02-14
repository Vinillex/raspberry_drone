from mpu6050 import mpu6050
from inv import INV
import time


mpu = mpu6050(0x68)
acc_x_multiplier = 0.973910471442764
acc_y_multiplier = 1.0096648591301125
acc_z_multiplier = 1.0291894394371972
acc_x_offset = 0.3314847553205471
acc_y_offset = -0.040665723867771675
acc_z_offset = 0.3552979334528086
gyr_x_offset = 1.3396946564885495
gyr_y_offset = -0.8893129770992366
gyr_z_offset = 1.1450381679389312

class MPU:

    def __init__(self) -> None:
        pass

    def getRawValues():
        accRaw = mpu.get_accel_data()
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
        accRaw = mpu.get_accel_data()
        gyrRaw = mpu.get_gyro_data()
        inv = INV(
        acc_x = (accRaw['x'] * acc_x_multiplier) + acc_x_offset,
        acc_y = (accRaw['y'] * acc_y_multiplier) + acc_y_offset,
        acc_z = (accRaw['z'] *  acc_z_multiplier) + acc_z_offset,
        #Gyroscope data is not callibrated as it's more precise and doesn't drift much
        gyr_x = gyrRaw['x'] + gyr_x_offset,
        gyr_y = gyrRaw['y'] + gyr_y_offset,
        gyr_z = gyrRaw['z'] + gyr_z_offset,
        )
        return inv

    
    

    
# while True:
#     MPU.getRawValues()
#     time.sleep(1)