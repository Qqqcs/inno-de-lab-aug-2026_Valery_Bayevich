import random 

number = random.randint(1, 20)
attempts = 5

print("Я загадал число от 1 до 20. У тебя есть 5 попыток, чтобы угадать его.")

while attempts > 0:
    guess = int(input("Попробуй угадать число: "))
    attempts -= 1

    if guess == number:
        print("Поздравляю! Ты угадал число!")
        break
    elif guess < number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")

    print(f"Осталось попыток: {attempts}")
else:
    print(f"К сожалению, ты не угадал число. Загаданное число было: {number}")

