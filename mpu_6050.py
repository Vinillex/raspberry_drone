import smbus
import matplotlib.pyplot as plt
import matplotlib.animation as animation

bus = smbus.SMBus(1)

address = 0x68
power_mnt = 0x6b

gyr_x_reg = 0x43
gyr_y_reg = 0x45
gyr_z_reg = 0x47

acc_x_reg = 0x3b
acc_y_reg = 0x3D
acc_z_reg = 0x3F

gyr_scale = 131.0
acc_scale = 16384.0

a_z = 0.9543361924410968
b_z = 0.25347045338846086
c_z = -0.9773114385696778
d_z = -4.361952416546307e-06
a_x = 0.9119440890628037
b_x = -0.052081100087172115
c_x = -0.8938773076929207
d_x = 7.316358807294149e-06
a_y = 0.9775800225055497
b_y = 0.06319780937694157
c_y = -0.9758370134130699
d_y = -2.8443337100954192e-06

# This function reads a word (two bytes) from an I2C device
# The word is read from the specified register address
# 
# Parameters:
#   reg (int): The register address to read the word from
# 
# Returns:
#   int: The word value read from the device
# 
def read_word(reg):
    # Read the high byte of the word from the specified register
    h = bus.read_byte_data(address, reg)
    
    # Read the low byte of the word from the specified register
    l = bus.read_byte_data(address, reg + 1)
    
    # Combine the high and low bytes to form the word value
    value = (h << 8) + l
    
    # Return the word value
    return value



# This function reads a word from a given register and returns its value.
# However, if the value is negative (i.e., greater than or equal to 0x8000),
# it converts it to a signed integer by performing two's complement arithmetic.

def read_word_2c(reg):
    # Read a word from the given register
    value = read_word(reg)

    # If the value is negative, convert it to a signed integer
    if value >= 0x8000:
        # Calculate the two's complement of the value
        complement = (65535 - value) + 1
        # Return the negative value
        return -complement
    else:
        # Otherwise, return the original value
        return value
    


# This function, `converted_acc(acc)`, is designed to convert a given acceleration value `acc` to a new scale.
# The conversion is achieved by dividing the input acceleration `acc` by a scaling factor `acc_scale`.
# The resulting value is then returned as the converted acceleration.
#
# Parameters:
# acc (float): The acceleration value to be converted.
#
# acc_scale (float): The scaling factor used for the conversion.
#
# Returns:
# float: The converted acceleration value.

def converted_acc(reg):
    # Divide the input acceleration by the scaling factor.
    converted_acc = read_word_2c(reg) / acc_scale    
    # Return the converted acceleration value.
    return converted_acc



# This function is used to convert the gyroscope data to a more usable form.
# The input to the function is 'gyr', which represents the raw gyroscope data.
# The function returns the converted gyroscope data, which is stored in the variable 'converted_gyr'.
# 
# The conversion is done by dividing the raw gyroscope data by 'gyr_scale', which is a constant value
# used for scaling the gyroscope data. This operation is performed in the line 'converted_gyr = gyr  / gyr_scale'.
# 
# This function is useful for processing and interpreting gyroscope data in a more meaningful way.
# It is important to note that the accuracy of the converted data depends on the correctness of the 'gyr_scale' value.

def converted_gyr(reg):
    # Convert the raw gyroscope data to a more usable form
    converted_gyr = read_word_2c(reg) / gyr_scale
    return converted_gyr


# This function calculates the raw acceleration data
def raw_acc():
    # Convert the raw acceleration values from the registers to m/s^2
    acc_x = converted_acc(acc_x_reg)
    acc_y = converted_acc(acc_y_reg)
    acc_z = converted_acc(acc_z_reg)

    # Return the acceleration values along the x, y, and z axes
    return {"x" : acc_x, "y" : acc_y, "z" : acc_z}


def raw_gyr():
    gyr_x = converted_gyr(gyr_x_reg)
    gyr_y = converted_gyr(gyr_y_reg)
    gyr_z = converted_gyr(gyr_z_reg)
    return {"x" : gyr_x, "y" : gyr_y, "z" : gyr_z}

def getOffset(x: float,y: float, z:float):
    offset_z = a_z * z ** 3 + b_z * z **2  + c_z * z + d_z
    offset_x = a_x * x ** 3 + b_x * x **2  + c_x * x + d_x
    offset_y = a_y * y ** 3 + b_y * y **2  + c_y * y + d_y
    offset = {
        "x":offset_x,
        "y":offset_y,
        "z":offset_z
    }
    return offset

def cal_acc():
    offset = getOffset(converted_acc(acc_x_reg),converted_acc(acc_y_reg),converted_acc(acc_z_reg))
    acc_x = converted_acc(acc_x_reg) + offset["x"]
    acc_y = converted_acc(acc_y_reg) + offset["y"]
    acc_z = converted_acc(acc_z_reg) + offset["z"]
    return {"x" : acc_x, "y" : acc_y, "z" : acc_z}


if __name__ == '__main__':

    bus.write_byte_data(address, power_mnt, 0)

    t_len = 200         # Number of points to display
    g_range = [-2, 2]  # Range of possible Y values to display

    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_ylim(g_range)

    t = list(range(0, 200))
    z = [0] * t_len
    x = [0] * t_len
    y = [0] * t_len


    # Create a blank line. We will update the line in animate
    line_z, = ax.plot(t, z,label = "gz")
    line_x, = ax.plot(t, x,label = "gx")
    line_y, = ax.plot(t, y,label = "gy")


    # Add labels
    plt.title('MPU 6050 Acceleration')
    plt.xlabel('Samples')
    plt.ylabel('Acceleration (m/s)')

    # This function is called periodically from FuncAnimation
    def animate(i, z , x, y):
        #acc_z = MPU.getCalibratedValues().acc_z
        #acc_x = MPU.getCalibratedValues().acc_x
        #acc_y = MPU.getCalibratedValues().acc_y

        acc_z = cal_acc()["z"]
        acc_x = cal_acc()["x"]
        acc_y = cal_acc()["y"]

        # Add y to list
        z.append(acc_z)
        x.append(acc_x)
        y.append(acc_y)


        # Limit y list to set number of items
        z = z[-t_len:]
        x = x[-t_len:]
        y = y[-t_len:]

        # Update line with new Y values
        line_z.set_ydata(z)
        line_x.set_ydata(x)
        line_y.set_ydata(y)

        return line_z,line_x,line_y,

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig,
        animate,
        fargs=(z,x,y),
        interval=50,
        cache_frame_data=False,
        blit=True)

    plt.legend()
    plt.show()


