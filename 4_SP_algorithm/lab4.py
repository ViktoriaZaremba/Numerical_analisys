import numpy as np
from math import sqrt

def file(f_name):
    #зчитує файл з елементами СЛАР та записує інформацію у матрицю  sys
    #f_name - назва файлу
    f = open(f_name)
    sys = []
    for line in f:
        row = [float(i) for i in line.split()]
        sys.append(row)
    return sys

def check_symmetric(array):
    checker = True
    for i in range(1, len(array)):
        for j in range(i):
            if array[i][j] != array[j][i]:
                checker = False
    return checker

def check_by_zero(array):
    checker = True
    for i in array:
        if i == 0:
            checker = False
    return checker

def result(a, resu):
    n = len(a)
    eps = a[-1][0]  # точність
    a = a[:-1]  # a - матриця
    n = n - 1
    y = [i for i in range(1, n+1)]   # довільний вектор
    k = 1   # лічильник

    # перевірка на симетрію і ненульовий векор
    if not check_symmetric(a):
        with open(resu, 'w', encoding="utf8") as f:
            f.write("Матриця не симетрична\n")
    if not check_by_zero(y):
        with open(resu, 'w', encoding="utf8") as f:
            f.write("Нульовий вектор\n")

    liam0 = 0   # лямбда0 для початкового порівняння
    a1 = np.linalg.inv(a)   # a1 - обернена матриця
    s0 = sum([i*i for i in y])  # скаляр S0
    y2 = sqrt(s0)   # норма вектора у
    x0 = [i/y2 for i in y]  # вектор х0
    yk = [0]*n

    while True:
        # обчислення вектора уk для обчислення найменшого за модулем числа А
        for i in range(n):
            s = 0
            for j in range(n):
                s+=a1[i][j] * x0[j]
            yk[i]=s
        sk = sum([i*i for i in yk])
        # обчислення вектора tk
        tk = 0
        for i in range(n):
            tk += yk[i]* x0[i]
        yk2 = sqrt(abs(sk))     # норма уk
        xk = [i/yk2 for i in yk]    # наближення до нормованого власного вектора
        liamk = sk/tk   # наближення до власного числа лямбда1
        if abs(liamk-liam0)>eps:
            k+=1
            liam0 = liamk
            x0 = np.copy(xk)
        else:
            break

    with open(resu, 'w', encoding="utf8") as f:
        f.write("Результат:\n")
        f.write("Найменше по модулю власне число: " + str(1/liamk))
        f.write("\nВідповідний власний вектор: " + str(xk))
        f.write('\nКількість ітерацій : ' + str(k))


result(file("Check1.txt"), "result1.txt")
result(file("Check2.txt"), "result2.txt")
