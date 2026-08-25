print("Простой калькулятор")
number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
task = input("Выберите операцию (+, -, *, /): ")

if task == "/" and number_2 == 0:
    print("Деление на ноль не поддерживается")
elif task == "+":
    print("Ответ:", number_1 + number_2)
elif task == "-":
    print("Ответ:", number_1 - number_2)
elif task == "*":
    print("Ответ:", number_1 * number_2)
elif task == "/":
    print("Ответ:", number_1 / number_2)
else:
    print("Неизвестная операция")