from sympy import *
import numpy as np
import math

def func(x):
    return x**2 - math.sin(math.pi * x)

def derivative(f, x, tol=1e-5):
    return (f(x + tol) - f (x - tol)) / (2 * tol)

def second_derivative(f, x, tol=1e-5):
    first_derivative = lambda x: derivative(f, x)
    return derivative(first_derivative, x)

print("Введіть а")
a = float(input())
print("Введіть b")
b = float(input())
eps = 1e-5

result = 0
if ((func(a)*func(b))>=0): #перевірка на умову
    print("func(a)*func(b) = ", func(a)*func(b))
    print("функція не віповідає вимогам методу")
    print('(НЕ "неперервна монотонна неліннійна функція, на відрізку [a, b] монотонна, диференційована і має єдиний корінь")')
if derivative(func, a)*second_derivative(func, a)>0 and derivative(func, a)*second_derivative(func, a)>0:
    x_res1 = 1
    x_res2 = -1
    b = 0
    while (True):
        x_res1 = x_res2 - (func(x_res2) * (b - x_res2)) / (func(b) - func(x_res2))
        if abs(x_res2 - x_res1) < eps:
            print(x_res1)
            break
        x_res2 = x_res1

    x_res1 = 1
    x_res2 = b
    while (True):
        x_res1 = a - (func(a) * (a - x_res2)) / (func(a) - func(x_res2))
        if abs(x_res2 - x_res1) < eps:
            result = x_res1
            print(result)
            break
        x_res2 = x_res1

if (func(b)*second_derivative(func, 0.9)) > 0:
    x_res1 = 1
    x_res2 = a
    while (True):
        x_res1 = x_res2 - (func(x_res2)*(b - x_res2))/(func(b) - func(x_res2))
        if abs(x_res2 - x_res1) < eps:
            print(x_res1)
            break
        x_res2 = x_res1
elif (func(a)*second_derivative(func, 0.9)) > 0:
    x_res1 = 1
    x_res2 = b
    while (True):
        x_res1 = a - (func(a) * (a - x_res2)) / (func(a) - func(x_res2))
        if abs(x_res2 - x_res1) < eps:
            result = x_res1
            print(result)
            break
        x_res2 = x_res1