def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    num = int(input("Введите число для вычисления факториала: "))
    if num < 0:
        print("Факториал не определен для отрицательных чисел!")
    else:
        print(f"Факториал {num} равен {factorial(num)}")
except ValueError:
    print("Пожалуйста, введите целое число!")