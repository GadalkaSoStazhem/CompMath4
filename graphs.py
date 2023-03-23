import numpy as np
import matplotlib.pyplot as plt
from calculations import *

def get_graphs(n, a, b, lin_func_before, lin_func_after, points_before):
    lim_x = max_x(points_before)
    lim_y = max_y(points_before)
    #plt.xlim([-(lim_x + 1), lim_x + 1])
    #plt.ylim([-(lim_y + 1), lim_y + 1])
    """ax = plt.gca()"""


    #fig, ax = plt.subplots()

    #ax.set(xlim=(-(lim_x + 1), lim_x + 1), xticks=np.arange(-(lim_x + 1), lim_x + 1),
           #ylim=(-(lim_y + 1), lim_y + 1), yticks=np.arange(-(lim_y + 1), lim_y + 1))
    """ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_aspect('equal')"""
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
    plt.show()