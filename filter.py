
from tkinter import W
import numpy as np

from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import *
import serial 

Serial = serial.Serial('COM6', baudrate=115200 )
TIME_OLD = 0
TIME_NEW = 0
dt = 0.
def read_sensor():
    TIME_OLD = TIME_NEW
    data = Serial.readline().decode("ütf-8")[:-2].split(";")
    TIME_NEW = data[1]
    return data


def S():
    a = []
    for i in range(100):
        a.append(read_sensor()[2])
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

while True:
    
    file = open("log.txt", "w")
    data = read_sensor()
    dt = TIME_NEW-TIME_OLD
    f.P = np.array([[1000.,dt ], [0., 1000.]])
    print(data)
    f.predict()
    f.update(data[2])
    x = []
    x.append(f.x[0])
    x.append(f.x[1])
    file.write(x)
    file.close()
