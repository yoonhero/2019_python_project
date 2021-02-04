import math
from math import pow, ceil
from matplotlib import pyploat as plt

gravity = 9.81
interval = 0.001

def timeArray(start, end, step):
    times = []
    while start < end:
        times.append(start)
        start += step
    return times

def draw_parabola(xVelocity, yVelocity):
    