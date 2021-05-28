import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# part 1
accel = pd.read_csv('/Users/manuja/Desktop/accel_file.txt', sep=",")

gyro = pd.read_csv('/Users/manuja/Desktop/gyro_file_5min.txt', sep=",")
sample = pd.read_csv('/Users/manuja/Desktop/sample.txt', sep=",", header=None)
print(accel.mean(axis=0))
accel.plot(kind='line',x='ts',y='x',color='red')
accel.plot(kind='line',x='ts',y='y',color='red')
accel.plot(kind='line',x='ts',y='z',color='red')
plt.show()


# part 2
import math
math.degrees(math.atan(1.18))
accel = pd.read_csv('/Users/manuja/Desktop/accel_file_5.txt', sep=",")
roll = np.arctan((accel['x'].values-6.899264e-04)/(accel['z'].values-0.0165))*180/np.pi
pitch = np.arctan((accel['y'].values+8.773818e-03)/(accel['z'].values-0.0165))*180/np.pi

x = np.arange(0,len(accel),1)*(1/60)
plt.title("Tilt Accelerometer")
plt.xlabel("Seconds")
plt.ylabel("Tilt")
plt.plot(x,roll, label='roll')
plt.plot(x,pitch, label='pitch')
plt.show()


dt = 1/60
gyro = pd.read_csv('/Users/manuja/Desktop/gyro_file_5.txt', sep=",")
print(gyro)
print(gyro['x'].values[0])
print(len(gyro))
omega_x = np.empty(len(gyro))
omega_y = np.empty(len(gyro))
omega_x[0] = (gyro['x'].values[0]+1.097152e-02)*dt
omega_y[0] = (gyro['y'].values[0]+8.390038e-03)*dt 
i = 1

for val in gyro['x'].values[1:len(gyro)-1]:
    omega_x[i] = omega_x[i-1] + (val+1.097152e-02)*dt
    i=i+1

i = 1
for val in gyro['y'].values[1:len(gyro)-1]:
    omega_y[i] = omega_y[i-1] + (val+8.390038e-03 )*dt
    i=i+1   

x = np.arange(0,len(gyro),1)*(1/60)
plt.title("Tilt from Gyrometer")
plt.xlabel("Seconds")
plt.ylabel("Tilt")
plt.plot(x,omega_x, label='roll')
plt.plot(x,omega_y, label='pitch')
plt.show()

# complementary filter

omega_x = np.empty(len(gyro))
omega_y = np.empty(len(gyro))
omega_x[0] = (gyro['x'].values[0]+1.097152e-02)*dt
omega_y[0] = (gyro['y'].values[0]+8.390038e-03)*dt 
i = 1

for val in gyro['x'].values[1:len(gyro)-1] :
    omega_x[i] = 0.98*(omega_x[i-1] + (val+1.097152e-02)*dt) + 0.02*roll[i]
    i=i+1

i = 1
for val in gyro['y'].values[1:len(gyro)-1]:
    omega_y[i] = 0.98*(omega_y[i-1] + (val+8.390038e-03 )*dt) + 0.02*pitch[i]
    i=i+1   

x = np.arange(0,len(gyro),1)*(1/60)
plt.title("Tilt from Gyrometer and Accelerometer")
plt.xlabel("Seconds")
plt.ylabel("Tilt")
plt.plot(x,omega_x, label='roll')
plt.plot(x,omega_y, label='pitch')
plt.legend()
plt.show()