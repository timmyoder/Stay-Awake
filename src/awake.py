import pyautogui
import time
import sys
from datetime import datetime
import random
import math
import numpy as np
import matplotlib.pyplot as plt

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.001
numMin = None

print('Never going to sleep')

try: 
    pause = int(float(sys.argv[1]))
except ValueError:
    raise ValueError('Pause must be convertable to an int')
except IndexError:
    raise IndexError('You must specifiy a length of time to pause')

def circle_points(radius, center):
    """creates list of points of a circle with specified radius"""
    angles = np.random.random(size=200) * 2*np.pi
    x = radius * np.cos(angles) + center[0]
    y = radius * np.sin(angles) + center[1]
    return x, y

while(True):
    time.sleep(random.randrange(pause))
    mouse_cur = pyautogui.position()
    x, y = circle_points(radius=100, center=mouse_cur)
    for i in range(0,random.randint(100, 200)):
        pyautogui.moveTo(x[i], y[i])
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
    