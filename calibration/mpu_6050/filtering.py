import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.append(parent_dir)

from mpu import MPU
import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq
import time

# Set the duration for the loop (in seconds)
DURATION = 5

N = 0  # For example, run the loop for 10 seconds

t_line = []
c_line = []

# Get the start time
start_time = time.time()



# Run the loop for the set duration              
while time.time() - start_time < DURATION:
    N += 1
    acc = MPU.getCalibratedValues().acc_z
    c_line.append(acc)

    
    # You can include more complex logic here
    
    # Pause for a short while to prevent high CPU usage

# After the loop finishes or the duration elapses, you can continue with the rest of your code
t_line = np.linspace(0, DURATION, N, endpoint=False)
c_array = np.array(c_line)
print("Loop finished!")
SAMPLE_RATE = int(N / DURATION)
print(SAMPLE_RATE)
print(N)
print(c_array)

normalized_tone = np.int16((c_array / c_array.max()) * 32767)

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.ylim([0,1.3*(10**5)])
plt.plot(xf,np.abs(yf))
plt.show()