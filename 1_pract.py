# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата. Сторону квадрата вводить с
# клавиатуры

import math #импорт математической бибилиотеки


def square(a):
    b = 4 * a #периметр
    c = a**2 #площадь
    # d = (2*(a**2))**(1/2) #диагональ квадрата, где **1/2 - извлечь квадратный корень
    d = math.sqrt(2*(a**2)) #sqrt - извлечь квадратный корень
    return b,c,d #если return, в любом случае кортеж ч/з запятую
print(square(4))