# При вводе десятизначного числа найти все четные числа в нем
# a = input('Введите 10-значное число: ')
# for i in a:
#     if (int(i)%2)==0:
#         print(i)

a = input('Введите 10-значное число: ')
c = ''
for i in a:
    if (int(i)%2)==0:
        c = c+i
print(c)
print(type(c))