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

def result(a, resu):
    n = len(a)
    x = [0] * (n-1)
    count = 0
    eps = a[-1][0]
    a = a[:-1]
    a2 = [[0] * (n-1) for i in range(n-1)]
    for i in range(n-1):
        for j in range(n-1):
            a2[i][j] = a[i][j]
    for i in range(n-1):
        for j in range(n-1):
            if not abs(a2[i][i])>=abs((sum(a2[i])-a2[i][i])):
                with open(resu, 'w', encoding="utf8") as f:
                    f.write("Матриця не має діагональної переваги.\nРозв'язати методом релаксації неможливо.\n")
                exit()
    a1 = [[0] * (n-1) for i in range(n-1)]
    b1 = [0] * (n-1)
    for i in range(n-1):
        for j in range(n-1):
            a1[i][j] = -(a[i][j]/a[i][i])
        b1[i] = a[i][-1]/a[i][i]

    x = [0] * (n-1)
    Rn = [0] * (n-1)
    Rp = [0] * (n-1)

    for i in range(n-1):
        s = 0
        for j in range(n-1):
            if i != j:
                s = s + a1[i][j]*x[j]
            Rp[i] = b1[i]-x[i]+s
    while True:
        maxR = -999
        maxIndex = 0
        for i in range(n-1):
            if abs(Rp[i])>maxR:
                maxR = abs(Rp[i])
                maxIndex = i

        for i in range(n-1):
            if i != maxIndex:
                Rn[i] = Rp[i] + a1[i][maxIndex]*Rp[maxIndex]
            else:
                Rn[i] = 0
                x[maxIndex] = x[maxIndex] + Rp[maxIndex]

        k = 0
        for i in range(n-1):
            if abs(Rn[i])<eps:
                k=k+1
            Rp[i]=Rn[i]

        if (k==(n-1)):
            break

    det = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                det = det * a[i][j]
    det = - pow(-1, count) * det
    d = np.linalg.det(a2)

    with open(resu, 'w', encoding="utf8") as f:
        f.write("Визначник:\n")
        f.write(str(d))
        f.write("\n\nРезультат:\n")
        if d != 0:
            for item in x:
                f.write(" %s\n" % item)
        else:
            f.write("однозначного розв'язку немає\n")
    return x



result(file("Check1.txt"), "result1.txt")
result(file("Check2.txt"), "result2.txt")
result(file("Check3.txt"), "result3.txt")
result(file("Check4.txt"), "result4.txt")