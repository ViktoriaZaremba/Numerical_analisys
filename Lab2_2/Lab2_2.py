from math import sqrt, ceil
import numpy as np

def file(f_name):
    #зчитує файл з елементами СЛАР та записує інформацію у матрицю  sys
    #f_name - назва файлу
    f = open(f_name)
    sys = []
    for line in f:
        row = [float(i) for i in line.split()]
        sys.append(row)
    return sys

def res(a, resu):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if not a[i][i]>(sum(a[i])-a[i][i]):
                with open(resu, 'w', encoding="utf8") as f:
                    f.write("Матриця не діагонально панівна.\nРозв'язати методом зустрічної прогонки неможливо.\n")
                exit()
    a1 = [0]*n
    c1 = [0]*n
    b1 = [0] * n
    x = [0] * n
    p = ceil(n/2)
    for i in range(n):
        for j in range(n):
            if j == i-1:
                a1[i] = a[i][j]
            if j == i+1:
                c1[i] = a[i][j]
        b1[i] = a[i][i]
    alf = [0] * n
    bet = [0] * n
    ep = [0] * n
    ny = [0] * n
    alf[0] = -c1[0]/b1[0]
    bet[0] = a[0][-1]/b1[0]
    ep[n-1] = -a1[n-1]/b1[n-1]
    ny[n-1] = a[n-1][-1]/b1[n-1]
    for i in range(int(p)):
        alf[i+1] = -c1[i]/(a1[i]*alf[i]+b1[i])
        bet[i+1] = (a[i][-1] - a1[i]*bet[i])/(b1[i]+alf[i]*a1[i])

    for i in range(n-1, int(p)+1, -1):
        ep[i] = -a1[i]/(b1[i]+c1[i]*ep[i+1])
        ny[i] = (a[i][-1] - c1[i]*ny[i+1])/(b1[i]+c1[i]*ep[i+1])

    x[p]= (ny[p]+ep[p]*bet[p])/(1-ep[p]*alf[p])
    x[p-1] = (bet[p]+alf[p]*ny[p])/(1-ep[p]*alf[p])
    for i in range(p-2, -1, -1):
        #x[i] = a[i][-1]-c1[i]*x[i+1]
        x[i] = alf[i+1]*x[i+1] + bet[i+1]

    for i in range(p, n-1):
        x[i+1] = ep[i+1]*x[i]+ny[i+1]

    # запис результатів у файл
    with open(resu, 'w', encoding="utf8") as f:
        f.write("\n\nРезульта   т:\n")
        for item in x:
            f.write(" %s\n" % item)
    return x


#res(file("Check1.txt"), "Result1.txt")
res(file("Check2.txt"), "Result2.txt")
#res(file("Check3.txt"), "Result3.txt")