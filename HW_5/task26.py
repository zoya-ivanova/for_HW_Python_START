# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Введите число А: "))  # 3
b = int(input("Введите число B: "))  # 5

def stepen(a, b):
    if b == 1:
        return a
    if b == 0 or a == 1:
        return 1
    return a * stepen(a, b-1)
print(stepen(3, 5))                  # 243

