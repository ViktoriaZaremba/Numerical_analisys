from numpy import *
import numpy as np
import copy


def derivative(f, x, tol=1e-5):
    return (f(x + tol) - f (x - tol)) / (2 * tol)

def jacobian(f, x):
    h = 1.0e-4
    n = len(x)
    Jac = zeros([n, n])
    f0 = f(x)
    for i in arange(0, n, 1):
        tt = x[i]
        x[i] = tt + h
        f1 = f(x)
        x[i] = tt
        Jac[:, i] = (f1 - f0) / h
    return Jac, f0


def jacobinewt(x):
    jjac = [[1, 2, 1, 4], [2 * x[0] + 2 * x[1], 2 * x[0], 0, 3 * x[3] ** 2],
            [3 * x[0] ** 2, 0, 2 * x[2], 1], [0, 3, x[3], x[2]]]
    # print(jjac)
    return (jjac)

def jac(f, x):
    for i in range(n):
        f[i] = derivative(f[i], x)
def f(x):
    # print(x)
    f = [x[0] + 2 * x[1] + x[2] + 4 * x[3], x[0] * x[0] + 2 * x[0] * x[1] + x[3] ** 3,
         x[0] ** 3 + x[2] ** 2 + x[3], 3 * x[1] + x[2] * x[3]]
    # print(f)
    return f


def matr_cheker(m):
    # Перевірка системи на однозначний розвязок
    # Приймає параметром матрицю
    # Повертає True якщо розвязку немає

    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False


def max_ell_in_column(m, col):
    # Замінює радок з найбільшим елементом (по модулю) основним рядком
    # Приймає параметром матрицю та індекс стовпця, в якому шукатиметься максимальний елемент
    # Нічого не повертає, лише змінює саму матрицю

    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
        # if abs(max_element) <= 0.00000001:
        #    print("No solution")
        #    exit()
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]


def gauss_method(m):
    # Розвязує матрицю методом Гауса з постовпцевим вибором головного елемента
    n = len(m)
    # Знаходження кількості перестановок рядків (для визначника)
    count = 0
    for k in range(n - 1):
        max_ell_in_column(m, k)
        for i in range(k + 1, n):
            index = m[i][k] / m[k][k]
            m[i][-1] -= index * m[k][-1]
            for j in range(k, n):
                m[i][j] -= index * m[k][j]
                count += 1

    # print("m",m)
    # Перевірка даної системи на однозначність
    # if matr_cheker(m):
    #    print("No solution")
    #    exit()
    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]
    return (x)

k = 0
n = 4
eps = 0.0001
#b = [ 20.7, 15.88, 21.218, 7.9 ]
b = [20.7, 15.88, 21.218, 21.1]
Bb = copy.deepcopy(b)
x0 = zeros([n])
g = copy.deepcopy(x0)
# print(x0)
for i in range(n):
    x0[i] = 1.0
print(x0, eps, b)
epss = 2 * eps
# x0=[1.2,5.6,4.3,1.0]
print(epss, ">", eps, k, g, "-", x0)
while ((epss > eps) and (k < 10)):
    print("iter k", k, "x0", x0)
    A = jacobinewt(x0)
    cf = f(x0)
    Bb = copy.deepcopy(b)
    print("b", b, "- cf", cf, Bb)
    for i in range(n):
        Bb[i] = Bb[i] - cf[i]

    print("A", A)
    print("Bb", Bb)
    print("b", b, "- cf", cf)
    mm = []
    # mm = [[]*n1 for i in range(n)]
    for i in range(n):
        bbb = A[i]
        bbb.append(Bb[i])
        # print("bbb",bbb)
        mm.append(bbb)
    # print("m",mm)

    g = gauss_method(mm)
    print("G", g)
    epss = 0
    for i in range(n):
        epss += g[i]
    epss = abs(epss)
    k += 1
    print("k", k, " ", epss, ">", eps, "g", g, "x0", x0)
    x0 += g
    print(x0)

print("end")
