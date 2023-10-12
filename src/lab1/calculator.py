#  PUT YOUR CODE HERE
from math import pow, sqrt


# + - / * ^ **
# main functions
def addition(x, y):
    '''addition of two numbers'''
    return x + y


def substraction(x, y):
    '''substraction of two numbers'''
    return x - y


def multiplication(x, y):
    '''multiplication of two numbers'''
    return x * y


def division(x, y):
    '''division of two numbers'''
    if y == 0:
        raise ValueError("Division by zero")
    return x / y


def power(x, y):
    '''power of two numbers'''
    if y < 0:
        raise ValueError("Must be positive")
    return pow(x, y)


def sqroot(x):
    '''sqroot of the number'''
    if x < 0:
        raise ValueError("Must be positive")
    return sqrt(x)


def continue_calc():
    '''check for continued operation of the calculator'''
    next_calculation = input("Хотите продолжить вычисления? (yes/no): ")
    if next_calculation == "no":
        print("До скорых встреч!")
        return False
    return True


def checking(exp):
    '''correct integer output'''
    if exp.is_integer():
        return int(exp)
    else:
        return exp


# main block
print("Добро пожаловать в калькулятор!")

calculation = True
while calculation is True:
    # all available operations
    print("Для сложения нажмите 1")
    print("Для вычитания нажмите 2")
    print("Для умножения нажмите 3")
    print("Для деления нажмите 4")
    print("Для возведения одного числа в степень другого числа нажмите 5")
    print("Для вычисления корня из числа нажмите 6")

    choice = input("Выберите нужную операцию (1, 2, 3, 4, 5, 6): ")

    # if we need in input two numbers
    if choice in ("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Введённое значение не корректно. Введите числа заново")
            continue

        # user choose one of that
        if choice == "1":
            res = addition(num1, num2)
            print(f"{num1} + {num2} = {round(checking(res), 10)}")

        if choice == "2":
            res = substraction(num1, num2)
            print(f"{num1} - {num2} = {round(checking(res), 10)}")

        if choice == "3":
            res = multiplication(num1, num2)
            print(f"{num1} * {num2} = {round(checking(res), 10)}")

        if choice == "4":
            res = division(num1, num2)
            try:
                print(f"{num1} / {num2} = {round(checking(res), 10)}")
            except ZeroDivisionError:
                print("Поделить на ноль не получится")

        if choice == "5":
            res = power(num1, num2)
            print(f"{num1} ** {num2} = {round(checking(res), 10)}")

        # continue or not
        calculation = continue_calc()

    # for sqroot only (one argument)
    elif choice in "6":
        try:
            num1 = int(input("Введите первое число: "))
        except ValueError:
            print("Введённое значение не корректно. Введите число заново")
            continue

        if num1 < 0:
            raise Exception("Число должно быть положительным")
        else:
            res = sqroot(num1)
            print(f"sqrt{num1} = {round(checking(res))}")

        # continue or not
        calculation = continue_calc()
    # incorrect input
    else:
        print("Неверный выбор. Пожалуйста, выберите значение из списка (1, 2, 3, 4, 5, 6).")
