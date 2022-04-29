a = [1,2,3,'hello','world']
b=[1,3,4,5,6,7]
a.append(7)
a.insert(1,7)
a[1]=3
c = a+b
b.extend(a)
print(a)
# a.remove('red')
# a.pop(10)
print(a.count(3))
d = a.copy()
d.append(5)
a.append(3)
print(d)
a.clear()
print(a)
# print(b)
# print(c)


f = [1,12,3,1,16,79,8,9]
f.reverse()
f.sort(reverse=True)
print(f)