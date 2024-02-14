from matplotlib import pyplot as plt
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU 

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
x_len = 200         # Number of points to display
y_range = [-15, 15]  # Range of possible Y values to display

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

    # Read temperature (Celsius) from TMP102
    temp_c = MPU.getRawValues().acc_x

    # Add y to list
    ys.append(temp_c)

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


# Create figure for plotting
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# xs = []
# ys = []

# # This function is called periodically from FuncAnimation
# def animate(i, xs, ys):

#     # Read temperature (Celsius) from TMP102
#     acc_x = MPU.getCalibratedValues().acc_x

#     # Add x and y to lists
#     xs.append(dt.datetime.now().strftime('%S.%f'))
#     ys.append(acc_x)

#     # Limit x and y lists to 20 items
#     xs = xs[-20:]
#     ys = ys[-20:]

#     # Draw x and y lists
#     ax.clear()
#     ax.plot(xs, ys)

#     # Format plot
#     plt.xticks(rotation=45, ha='right')
#     plt.title('Acceleration with Time')
#     plt.ylabel('Acceleration')

# # Set up plot to call animate() function periodically
# ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1,frames=60)
# plt.show()