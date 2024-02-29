from mpu6050 import mpu6050
from inv import INV
from mpu_offset import  MPUOffset

mpu = mpu6050(0x68)

a_z = 0.9626295226404501
b_z = 0.2817230778933209
c_z = -0.9775939282748225
d_z = -3.7913214639210853e-06
a_x = 1.0119922807680832
b_x = -0.06451982514935464
c_x = -0.9795071601327258
d_x = 2.76090288997903e-06
a_y = 0.965796970250293
b_y = 0.06236784323925405
c_y = -0.9669709967470123
d_y = -4.945512228834201e-06

#a_z = 0.20977510492859303
#b_z = -0.009279854912595678
#c_z = -0.0004513226536026327
#a_x = -0.05447038442995004
#b_x = 0.003962473751550104
#c_x = 0.00011353191633228821
#a_y = 0.08100281170035768
#b_y = -0.0027857145959767006
#c_y = -0.00020438220780932028

def getOffset(x: float,y: float, z:float):
    offset_z = a_z * z ** 3 + b_z * z **2  + c_z * z + d_z
    offset_x = a_x * x ** 3 + b_x * x **2  + c_x * x + d_x
    offset_y = a_y * y ** 3 + b_y * y **2  + c_y * y + d_y
    offset = MPUOffset(
    acc_o_x = offset_x,
    acc_o_y = offset_y,
    acc_o_z = offset_z,
    gyr_o_x=0,
    gyr_o_y=0,
    gyr_o_z=0
    )
    return offset

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
        calibrated_offset = getOffset(accRaw['x'],accRaw['y'],accRaw['z'])
        inv = INV(
        acc_x = accRaw['x'] + calibrated_offset.acc_o_x,
        acc_y = accRaw['y'] + calibrated_offset.acc_o_y,
        acc_z = accRaw['z'] + calibrated_offset.acc_o_z,
        #Gyroscope data is not callibrated as it's more precise and doesn't drift much
        gyr_x = gyrRaw['x'],
        gyr_y = gyrRaw['y'],
        gyr_z = gyrRaw['z'],
        )
        return inv
    
    

