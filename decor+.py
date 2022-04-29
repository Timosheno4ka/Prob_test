#декораторы
from datetime import datetime

def timeit(func): #1 func - любое название
    def wrapper(*args, **kwargs):     #3
        start = datetime.now() #6
        result = func(*args, **kwargs)   #5
        print(datetime.now() - start) #7
        return result    #4

    return wrapper #2 wrapper - любое название

@timeit ()#8
def one(n):
    l = []
    for i in range(n):
        if i %2==0:
            l.append(i)
    return l

@timeit() #9
def two(n):
    l = [x for x in range(n) if x%2 ==0]
    return l

# l1 = one(1000)
# l2 = two(1000)
#
# print(l1)
# print(l2)

#Объект функции
# l1 = one #передали ОБЪЕКТ функции (без скобок()), а не результат ее работы, L1 стал функцией
# a = l1(10) #вызвали функцию L1  и передали в нее позиционный аргумент 10
# print(a)

# l1 = timeit(one)(10) # такая конструкция возвращает => wrapper(10) => one(10)
# print(type(l1), l1.__name__)
# a = l1(10)