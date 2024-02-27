import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU

# Parameters
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

    acc_z = MPU.getCalibratedValues().acc_z
    acc_x = MPU.getCalibratedValues().acc_x
    acc_y = MPU.getCalibratedValues().acc_y

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