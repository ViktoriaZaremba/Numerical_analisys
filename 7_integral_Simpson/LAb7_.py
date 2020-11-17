from math import *
import numpy as np
import math


def f1(x):
    return ((x + 3.8)**3)/(3.3 * x*x + 5.5*x + 2.2)


def f2(x):
    return ((x ** 4 + 1)*(x ** 2 + 2.7))/((x + 0.9)*(x ** 2 + 2.1))


def simpson(a, b, n):
    e = 1
    h = (b - a)/(2*n)
    s = f1(a)-f1(b)
    for i in range(1, 2*n):
        s += (3+e)*f1(a+i*h)
        e = -e

    s = s*(h/3)
    return s


eps = 0.5e-5
a = float(input())
b = float(input())
n = int(input())


while(math.fabs(simpson(a, b, n) - simpson(a, b, n*2))>eps):
    n *= 2

print(simpson(a, b, n))
print(str(n))