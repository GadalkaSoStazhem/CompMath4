def get_number():
    number = int(input("Введите номер примера: "))
    if number < 1 or number > 4:
        print("Неверный номер примера")
        return None
    return number


def print_function(number):
    print("Выбранная функция:")
    if number == 1:
        print("y(x) = (x - 3)^(1/3) + 3")
    elif number == 2:
        print("y(x) = log2(x - 1)")
    elif number == 3:
        print("y(x) = 0.3 * x * sin(x)")
    elif number == 4:
        print("y(x) = x^4 + 2x")

def print_points(points):
    print("Набор точек: ")
    for i in range (len(points)):
        if (i == 0):
            print("       x       y")
        print("%3d |" % (i + 1), end = "")
        for j in range(2):
            if nice_io(points[i][j]):
                print("%.3f " % (points[i][j]), end="")
            else:
                print("%4d  " % int(points[i][j]), end="")
        print()

def nice_io(number):
    if (abs(abs(round(number)) - abs(number)) < 0.00000001):
        return False
    return True
