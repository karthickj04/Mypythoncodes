import sys


def sum1(a, b):
    w = a + b
    return w


def sub(a, b):
    u = a - b
    return u


def mult(a, b):
    z = a * b
    return z


def average():
    v = sum1(x, y)/2
    return v


def exponential(a, b):
    i = a ** b
    return i


lst = sys.argv
x = int(lst[1])
y = int(lst[2])
print("The Sum of two numbers is ", sum1(x, y))
print("The Subtracted of two numbers is ", sub(x, y))
print("The Multiplied value of two numbers is ", mult(x, y))
print("The Average of two numbers is ", average())
print('The Exponential of ', x, ' power ', y, "is ", exponential(x, y))
