#Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

def decor(func):
    i=0
    def wrapper():
        nonlocal i
        func()
        i+=1
        print(f'{i}')
    return wrapper

@decor
def hello():
    print("Hello!")

hello()
hello()


