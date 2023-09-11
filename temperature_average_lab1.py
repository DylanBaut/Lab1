from sense_hat import SenseHat
from time import sleep
import math
import matplotlib.pyplot as plt

sense = SenseHat()
sense.clear() ## to clear the LED matrix

temperature=sense.get_temperature()
temp_changed = False


temperatures = []
normal = []
# Will run for 10 seconds:
for i in range(20):
    tenth_second = []
    for j in range(50):
        curr_temperature = sense.get_temperature()
        if j == 0:
            normal.append(curr_temperature)
        tenth_second.append(curr_temperature)
        sleep(0.01)
    temperatures.append(tenth_second)
    
averaged = [sum(x)/len(x) for x in temperatures]
times = [0.5 * x for x in range(20)]

# plt.hold()
plt.plot(times, averaged)
plt.plot(times, normal)
plt.xlabel('time in seconds')
plt.ylabel('temperature in C')
plt.legend(["averaged", "normal"])
plt.show()

print(averaged)
        
