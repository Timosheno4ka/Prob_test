# 1. Создайте функцию, добавьте в неё локальное значение. Сделайте так, чтобы другая функция принимала это
# значение в качестве параметра.
# 2.  Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

# def func_1():
#     global a
#     a = 8
#     return a
#
# def func_2():
#     b = 2
#     return a+b
#
# print(f'Значение первой функции: {func_1()}')
# print(f'Сумма значений 1 и 2 функций: {func_2()}')

def is_prime(a):
    if a < 2: #0 и 1 не являются простыми числами
        return False
    for i in range(2, int(a ** 0.5 + 1)): #**0.5 - извлечь корень из числа а
        if a % i == 0:
            return False
    else:
        return True
print(is_prime(int(input('Введите число от 0 до 1000: '))))
