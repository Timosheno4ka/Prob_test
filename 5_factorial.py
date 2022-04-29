def factorial(n):
    if n !=0: # граничный случай
        print(n)
        return n*factorial(n-1) #рекурсивный, вызывает саму себя
    else:
        return 1

print(factorial(5))

# product = lambda x,y: x+y
# print(product(2,1))