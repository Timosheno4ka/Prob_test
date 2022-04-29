def func():
    global a
    a = 5
    return a+6

def func_2():
    return a+10

print(func())
print(func_2())
