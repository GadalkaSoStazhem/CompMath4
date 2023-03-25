from my_io import *
from functions import *
from checker import *
from least_square import *
from graphs import *

number = get_number()
if number != None:
    print_function(number)
    func = get_function(number)
    left, right = [float(x) for x in input("Введите интервал для аппроксимации: ").split()]
    if (interval_check(left, right)):
        n = int(input("Введите количество точек: "))
        func_points = get_points(left, right, n, func)
        print_points(func_points)
        lin_func, a, b = get_linear_function(func_points, n)
        print("Линейная аппроксимирующая функция до исключения точки с максимальным квадратом отклонения:")
        print("y(x) = ", "%.4f" % (a), "x + ", "(%.4f)" % (b))
        sigma = get_error(func_points, lin_func)
        print("Погрешность: ", sigma)
        index, max_dif = point_to_remove(func_points, lin_func)
        print("Максимальный квадрат отклонения (%.4f)" %(max_dif)," у точки №", (index + 1))
        old_points = func_points.copy()
        func_points.pop(index)
        lin_func1, a_new, b_new = get_linear_function(func_points, n - 1)
        print("Линейная аппроксимирующая функция после исключения точки №", index,"и пересчета:")
        print("y(x) = ", "%.4f" % (a_new), "x + ", "(%.4f)" % (b_new))
        sigma = get_error(func_points, lin_func1)
        print("Погрешность: ", sigma)
        get_graphs(n, left, right, lin_func, lin_func1, old_points)



