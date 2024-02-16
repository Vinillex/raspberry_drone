import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU

# Parameters
x_len = 200         # Number of points to display
y_range = [-2, 2]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('MPU 6050 Acceleration')
plt.xlabel('Samples')
plt.ylabel('Acceleration (m/s)')

# This function is called periodically from FuncAnimation
def animate(i, ys):
    acc_z = MPU.getCalibratedValues().acc_z

    # Add y to list
    ys.append(acc_z)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=50,
    cache_frame_data=False,
    blit=True)
plt.show()