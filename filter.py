import horizon
from tkinter import W
import numpy as np

from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import *
import serial 

Serial = serial.Serial('COM4', baudrate=9600 )
TIME_OLD = 0
TIME_NEW = 0
dt = 0.
def read_sensor():
    data = Serial.readline().decode("utf-8")[:-2].split(";")
    print(data)
    return data


def S():
    a = []
    for i in range(100):
        a.append(float(read_sensor()[2]))
    print(a)
    f.R = np.std(a)
    print("Эта фигня найдена")
def start():
    for i in range(3):
        print(Serial.readline().decode("utf-8"))
start()
f = KalmanFilter (dim_x=2, dim_z=1)
f.x = np.array([0., 0.])

f.H = np.array([[1.,0.]])
f.P *= 1000.
S()
f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13)
s = []
for i in range(200):
    TIME_OLD = TIME_NEW
    
    
    
    data = read_sensor()
    TIME_NEW = float(data[1])
    dt = TIME_NEW-TIME_OLD
    f.P = np.array([[1000.,dt ], [0., 1000.]])
    horizon.rotate(float(data[-3]))
    print(data)
    f.predict()
    f.update(float(data[2]))
    x = []
    x.append(f.x[0])
    x.append(f.x[1])
    s.append(x)
file = open("lxg.txt", "w")
file.write(str(s))
file.close()