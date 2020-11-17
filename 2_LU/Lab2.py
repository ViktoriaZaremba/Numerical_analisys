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

def count_func(a, resu):
    n = len(a)
    x = [0] * n
    count = 0
    for i in range(n-1):
        for k in range(i+1, n):
            c = a[i][i] / sqrt(a[i][i] ** 2 + a[k][i] ** 2)
            s = a[k][i] / sqrt(a[i][i] ** 2 + a[k][i] ** 2)
            z0 = c ** 2 + s ** 2
            temp1 = [0] * (n + 1)
            for j in range(i, n+1):
                a1 = a[i][j]
                a2 = a[k][j]
                a[i][j]=c*a1 + s * a2
                a[k][j]= -s*a1 + c *a2
                count += 1

        # визначник
    det = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                det = det * a[i][j]
    det = - pow(-1, count) * det

    # зворотній хід
    if det != 0:
        x[n-1] = a[n-1][-1]/a[n-1][n-1]
        for k in range(n-1, -1, -1): #8
            x[k] = (a[k][-1] - sum([a[k][j] * x[j] for j in range(k+1, n)])) / a[k][k] #9

    # запис результатів у файл
    with open(resu, 'w', encoding="utf8") as f:
        f.write("Визначник:\n")
        f.write(str(det))
        f.write("\n\nРезультат:\n")
        if det != 0:
            for item in x:
                f.write(" %s\n" % item)
        else:
            f.write("однозначного розв'язку немає\n")
    return x

count_func(file("Check1_2.txt"), "Result1_2.txt")
count_func(file("Check1_3.txt"), "Result1_3.txt")
count_func(file("Check1_4.txt"), "Result1_4.txt")