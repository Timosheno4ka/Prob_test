#Матрешка
# def matryoshka(n): #n - кол-во матрешек, которые нужно напечатать Matroshka - имя мастера, который должен выполнить работу
#     if n == 1:
#         print('Матрешечка') # проверить если это крайняя матрешка (крайний случай)
#     else:
#         print('Верх матрешки n=', n)
#         matryoshka(n-1)
#         print('Низ матрешки n=', n)
# matryoshka(5)

#Факториал
# def f(n): #n - целое число
#     assert n>=0, "Факториал отрицательногшо не определен" #asserrt - оператор утверждения
#     if n ==0:
#         return 1
#     #здесь можно не писать else, тк. если мы здесь оказались, значит n уже не равен 0 (после if)
#     return f(n-1)*n  #здесь есть приоритетное действие n-1, значит это действие происходит ДО рекурсии

#Алгоритм Евклида найти наибольший общий делитель двух отрезков а - длиннее, b - короче
# def gcd(a,b):
#     if a ==b:
#         return a
#     elif a>b:
#         return gcd(a-b,b)
#     else: #a<b
#         return gcd(a,b-a)

#или
# def gcd(a,b):
#     if b ==0:
#         return a
#     else:
#         return gcd(b,a%b)

#или короче
# def gcd(a,b):
#     return a  if b == 0 else gcd(b,a%b)

#Быстрое возведение в степень
# def pow(a: float,n: int):
#     if n ==0:
#         return 1
#     else:
#         return pow(a,n-1)*a

#Если степень четная
# def pow(a: float,n: int): #a в степени n  = (a**2)n//2
#     if n ==0:
#         return 1
#     elif n%2 ==1: # для нечетных
#         return pow(a,n-1)*a
#     else:# n - четная
#         return pow(a**2,n//2)

#Ханойские башни




