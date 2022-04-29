a = {1,3,4,2,8,3}
b = frozenset([2,17,3,4,9,5])
x=0
# Проверить, есть ли в последовательности чисел списка дубликаты.

print(a.isdisjoint(b))
print(f'Дубликаты в a и b: {a & b}')
print(f'Дубликаты в a и b: {a.intersection(b)}')