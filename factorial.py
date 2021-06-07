import math

def factorial(n):
    productoria = 1
    i = 2
    while i <= n:
        productoria *= i
        i+=1
    return productoria 