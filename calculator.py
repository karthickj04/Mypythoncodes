import sys


def sum1(a, b):
    x = a + b
    return x


def sub(a, b):
    y = a - b
    return y


def mult(a, b):
    z = a * b
    return z


lst = sys.argv
a = int(lst[1])
b = int(lst[2])
print("The Sum of two numbers is", sum1(a, b))
print("The Subtracted of two numbers is", sub(a, b))
print("The Multiplied value of two numbers is", mult(a, b))
