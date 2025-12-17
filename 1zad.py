# x = int(input("x = ")) (ЛЕКЦИЯ)
# y = int(input("y = "))
#
# if (x + y) % 2 == 0:
#     print("ч")
# else:
#     print("б")
#2 (1.	Шахматный конь ходит буквой "Г" )
from math import factorial

# k1 = int(input("k1 = "))
# k2 = int(input("k2 = "))
# n1 = int(input("n1 = "))
# n2 = int(input("n2 = "))
#
#
# if not (1 <= k1 <= 8 and 1 <= k2 <= 8 and 1 <= n1 <= 8 and 1 <= n2 <= 8):
#     print("Ошибка!")
# else:
#     if (abs(k1 - n1) == 2 and abs(k2 - n2) == 1) or (abs(k1 - n1) == 1 and abs(k2 - n2) == 2):
#         print("Да")
#     else:
#         print("Нет")

#3 (2.	Пользователь вводит числа K и N)
#
# k = int(input("сумма k ="))
# n = int(input("сумма n ="))
# sum = 0
# for i in range(k, n + 1):
#     if i % 2 == 0:
#         sum += i
#
# print("Сумма четных чисел:", sum)

#4(3.	Пользователь вводит числа до тех пор, пока не введет 0. )
# sum = 0
# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         break
#     sum += num
#
# print("Сумма введенных чисел:", sum)

#5(4.	Пользователь вводит число N. Выведите факториал число N. )
#
# N = int(input("Введите число N: "))
# factorial = 1
# for i in range(1, N + 1):
#     factorial *= i
#
# print("Факториал числа", N, "равен:", factorial)