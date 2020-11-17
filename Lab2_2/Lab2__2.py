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

def res(a, resu):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if not a[i][i]>(sum(a[i])-a[i][i]):
                with open(resu, 'w', encoding="utf8") as f:
                    f.write("Матриця не діагонально п.\nРозв'язати методом зустрічної прогонки неможливо.\n")
                exit();

    a1 = [0]*n
    c1 = [0]*n
    b1 = [0] * n
    x = [0] * n
    p = n/2
    for i in range(n):
        for j in range(n):
            if j == i-1:
                a1[i] = a[i][j]
            if j == i+1:
                c1[i] = a[i][j]
        b1[i] = a[i][i]
    alf = [0] * n
    bet = [0] * n
    alf[0] = -c1[0]/b1[0]
    bet[0] = a[0][-1]/b1[0]
    for i in range(1, n):
        alf[i] = -c1[i]/(a1[i]*alf[i-1]+b1[i])
        bet[i] = (a[i][-1] - a1[i]*bet[i-1])/(a1[i]*alf[i-1]+b1[i])

    x[n-1] = (a[n-1][-1]-a1[n-1]*bet[n-2])/(a1[n-1]*alf[n-2]+b1[n-1])
    for i in range(n-2, -1, -1):
        #x[i] = a[i][-1]-c1[i]*x[i+1]
        x[i] = alf[i]*x[i+1] + bet[i]

    # запис результатів у файл
    with open(resu, 'w', encoding="utf8") as f:
        f.write("\n\nРезультат:\n")
        for item in x:
            f.write(" %s\n" % item)
    return x


res(file("Check1.txt"), "Result1.txt")
#res(file("Check2.txt"), "Result2.txt")
res(file("Check3.txt"), "Result3.txt")