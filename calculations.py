def get_step(a, b, n):
    return (b - a) / n


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


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


def get_error(points, lin_func):
    sigma = 0
    for row in points:
        sigma += (row[1] - lin_func(row[0]))**2
    return sigma
