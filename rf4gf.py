import random

number = random.randint(1, 100)
attempts = 0

print("Угадайте число от 1 до 100!")
while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1
    if guess < number:
        print("Слишком мало!")
    elif guess > number:
        print("Слишком много!")
    else:
        print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток!")
        break