import numpy as np
import matplotlib.pyplot as plt
from calculations import *
from least_square import *

def get_graphs(n, a, b, lin_func_before, lin_func_after, points_before):
    plt.grid(True)
    x = np.arange(a, b + 1, 1)
    y2 = lin_func_before
    y3 = lin_func_after
    xs1 = x_array(points_before)
    ys1 = y_array(points_before)
    plt.scatter(xs1, ys1, color = 'black', label = 'начальные точки')
    plt.plot(x, y3(x), 'g', label = 'до исключения')
    plt.plot(x, y2(x), 'b', label = 'после исключения и пересчета')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()