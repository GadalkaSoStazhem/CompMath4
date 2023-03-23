import numpy as np
from calculations import *
def get_function(number):
    if number == 1:
        return lambda x: sign(x - 3) * (abs(x - 3))**(1./3.) + 3
    elif number == 2:
        return lambda x: np.log2(x - 1)

def get_points(a, b, n, func):
    step = get_step(a, b ,n)
    points = []
    for i in range (n):
        row = [a, func(a)]
        points.append(row)
        a += step
    return points

