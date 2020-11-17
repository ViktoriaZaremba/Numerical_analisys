import numpy as np
import math
import sympy as sym

def derivative(f, x, tol=1e-5):
    return (f(x + tol) - f (x - tol)) / (2 * tol)

def second_derivative(f, x, tol=1e-5):
    first_derivative = lambda x: derivative(f, x)
    return derivative(first_derivative, x)

def equation(x):
    return x**2 - math.cos(math.pi*x)

def functiona(a, b):
    return a - (equation(a)*(b - a))/(equation(b) - equation(a))

def functionb(a, b):
    return b - (equation(b)*(b - a))/(equation(b) - equation(a))

def chords_for_B(a, b, eps=1e-3):
    x = 1
    x_new = b
    while(True):
        x = functionb(x_new, a)
        if abs(x_new - x) < eps:
            return x
        x_new = x

def chords_for_A(a, b, eps=1e-3):
    x = 1
    x_new = a
    while(True):
        x = functiona(x_new, b)
        if abs(x_new - x) < eps:
            return x
        x_new = x

print("Введіть а")
a = float(input())
print("Введіть b")
b = float(input())
eps = 1e-5
if a == b:
    print("ERROR")
    exit(0)
if a < -0.5 and b < -0.5:
    print("ERROR")
    exit(0)
if a > 0.5 and b > 0.5:
    print("ERROR")
    exit(0)
if derivative(equation, a)*second_derivative(equation, a) > 0 and derivative(equation, b)*second_derivative(equation, b) < 0 or a == -b:
    #print("For interval " + str(a) +' to 0 ')
    print(chords_for_A(-1, 0))
    #print("For interval "+ '0 to ' + str(b))
    print(chords_for_B(1, 0))
    exit()
if equation(b)* second_derivative(equation, 0.5) > 0:
    print(chords_for_A(a, b))
elif equation(a)*second_derivative(equation, 0.5) > 0:
    print(chords_for_B(a, b))

