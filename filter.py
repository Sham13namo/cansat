
import numpy as np
import matplotlib as plt
from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import *
import serial 

Serial = serial.Serial('COM6', baudrate=115200 )
TIME_OLD = 0
TIME_NEW = 0
dt = 0.
def read_sensor():
    data = Serial.readline().decode("ütf-8")[:-2].split(";")
    

def S():
    a = []
    for i in range(100):
        a.append(read_sensor())
    f.R = np.std(a)
    print("Эта фигня найдена")
def start():
    for i in range(3):
        print(Serial.readline().decode("utf-8"))
start()
f = KalmanFilter (dim_x=2, dim_z=1)
f.x = np.array([0., 0.])
f.P = np.array([[1000.,dt ], [0., 1000.]])
f.H = np.array([[1.,0.]])
f.P *= 1000.
S()
f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13)
s = []
raw  = []

for i in range(120):
    z = read_sensor()
    raw.append(z)
    f.predict()
    f.update(z)
    x = []
    x.append(f.x[0])
    x.append(f.x[1])
    s.append(x[0])
print(raw)
print(s)
