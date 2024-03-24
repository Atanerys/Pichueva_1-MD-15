def di():
    try:
        n = float(input("Введите число для деления 100: "))
        result = 100 / int(n)
        print("Результат деления 100 на " + str(n) + " равен" +  str(result))
    except ValueError:
        print("Ошибка: Введено не число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")

di()
