print("Простой калькулятор")
number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
task = input("Выберите операцию (+, -, *, /): ")

print("Ответ:", (number_1 + number_2 if task == "+" else
                 number_1 - number_2 if task == "-" else
                 number_1 * number_2 if task == "*" else
                 number_1 / number_2 if task == "/" else None))