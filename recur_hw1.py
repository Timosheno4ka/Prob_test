# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
# Рекурсивная функция - возвращает сумму чисел во входящем наборе

import random
n = [random.randint(1,100) for i in range(10)] # 1. Создать набор чисел
print(n)
# def numb(a):
#     if a ==[]:
#         return 0
#     else:
#         a = sum(a[:])
#         return a
#
#
# print('Сумма чисел списка: ', numb(n))
# def numb(a):
#     if a ==[]:
#         return 0
#     else:
#         a = n[:]
#         a = sum(n)
#         return a
#
#
# print('Сумма чисел списка: ', numb(n))


