def get_number():
    number = int(input("Введите номер примера: "))
    if number < 1 or number > 2:
        print("Неверный номер примера")
        return None
    return number


def print_function(number):
    print("Выбранная функция:")
    if number == 1:
        print("y(x) = (x - 3)^(1/3) + 3")
    elif number == 2:
        print("y(x) = log2(x - 1)")
