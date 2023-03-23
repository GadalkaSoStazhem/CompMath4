from calculations import *

def get_linear_function(points, n):
    a = (n * sum_xy(points) - sum_x_or_y(points, 0) * sum_x_or_y(points, 1)) / (n * sum_kv_x(points) - sum_x_or_y(points, 0) ** 2)
    b = (sum_x_or_y(points, 1) - a * sum_x_or_y(points, 0)) / n
    return lambda x: a * x + b, a, b
