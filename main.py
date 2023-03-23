from my_io import *
from functions import *
from checker import *
from least_square import *
from graphs import *

number = get_number()
print_function(number)
func = get_function(number)
a, b = [int(x) for x in input("Введите интервал для аппроксимации: ").split()]
if (interval_check(a, b)):
    n = int(input("Введите количество точек: "))
    func_points = get_points(a, b, n, func)
    print(func_points)
    lin_func = get_linear_function(func_points, n)
    index = point_to_remove(func_points, lin_func)
    print(index)
    old_points = func_points.copy()
    print("old", len(func_points))
    func_points.pop(index)
    print("new", len(func_points))
    lin_func1 = get_linear_function(func_points, n - 1)
    get_graphs(n, a, b, lin_func, lin_func1, old_points)


