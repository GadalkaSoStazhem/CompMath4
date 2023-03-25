def interval_check(a, b):
    if a >= b:
        print ("Неверный интервал")
        return False
    return True

def point_to_remove(points, lin_func):
    index = 0
    cnt = 0
    max_dif = 0
    error = 0
    for row in points:
        sigma = (row[1] - lin_func(row[0])) ** 2
        error += sigma
        if sigma > max_dif:
            max_dif = sigma
            index = cnt
        cnt += 1
    return index, max_dif

