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
r = [0] * t_len
c = [0] * t_len


# Create a blank line. We will update the line in animate
line_r, = ax.plot(t, r,label = "gr")
line_c, = ax.plot(t, c,label = "gc")


# Add labels
plt.title('MPU 6050 Acceleration')
plt.xlabel('Samples')
plt.ylabel('Acceleration (m/s)')

# This function is called periodically from FuncAnimation
def animate(i, r , c):

    acc_r = MPU.getRawValues().acc_z
    acc_c = MPU.getCalibratedValues().acc_z

    #if(acc_c > 0):
     #   acc_c = acc_c ** (1./3.)
    #else:
     #   acc_c = -((-acc_c) ** (1./3.))

    # Add y to list
    r.append(acc_r)
    c.append(acc_c)


    # Limit y list to set number of items
    r = r[-t_len:]
    c = c[-t_len:]

    # Update line with new Y values
    line_r.set_ydata(r)
    line_c.set_ydata(c)

    return line_r,line_c,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(r,c),
    interval=50,
    cache_frame_data=False,
    blit=True)

plt.legend()
plt.show()