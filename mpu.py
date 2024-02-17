from mpu6050 import mpu6050
from inv import INV

mpu = mpu6050(0x68)

acc_x_multiplier = 0.9948828125
acc_y_multiplier = 0.99984619140625
acc_z_multiplier = 1.01486572265625
acc_x_offset = 0.013611653645833333
acc_y_offset = -0.01932861328125
acc_z_offset = -0.076376953125

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
        acc_z = (accRaw['z'] * acc_z_multiplier) + acc_z_offset + 0.02,
        #Gyroscope data is not callibrated as it's more precise and doesn't drift much
        gyr_x = gyrRaw['x'] + gyr_x_offset,
        gyr_y = gyrRaw['y'] + gyr_y_offset,
        gyr_z = gyrRaw['z'] + gyr_z_offset,
        )
        return inv
