# список из 7 цифр. Если четных больше, чем нечетных, то найти сумму (произведение) всех цифр.
# Если нет, то произведение 1,3 и 6 элементов

a = [6,2,3,4,5,6,7]
b = 0
c = 0
f = 1
for i in a:
    if i%2 ==0:
       b+=1#b=b+1
    else:
        c+=1
if b>c:
    # f = sum(a)
    for i in a:
        f = f * i
    print(f)
else:
    r = a[0]*a[2]*a[5]
    print(r)