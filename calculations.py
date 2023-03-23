def get_step(a, b, n):
    return (b - a) / n
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def sum_xy (points):
    summa = 0
    for row in points:
        summa += (row[0] * row[1])
    return summa

def sum_x_or_y (points, num):
    summa = 0
    for row in points:
        summa += row[num]
    return summa

def sum_kv_x (points):
    summa = 0
    for row in points:
        summa += row[0] ** 2
    return summa

def x_array(points):
    xs = []
    for row in points:
        xs.append(row[0])
    return xs

def y_array(points):
    ys = []
    for row in points:
        ys.append(row[1])
    return ys

def max_y (points):
    y = 0
    for row in points:
        y = max(y, abs(row[1]))
    return y
def max_x(points):
    x = 0
    for row in points:
        x = max(x, abs(row[0]))
    return x
