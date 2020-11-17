from math import sqrt

def file(f_name):
    # зчитує файл з елементами СЛАР та записує інформацію у матрицю  sys
    # f_name - назва файлу
    f = open(f_name)
    sys = []
    for line in f:
        row = [float(i) for i in line.split()]
        sys.append(row)
    return sys

def norm(a, resu):
    n = len(a)
    m = n + 1
    suma = []
    for i in range(n):
        for j in range(n):
            a[i][j] = abs(a[i][j])
            suma.append(sum(a[i]) - a[i][-1])
    norm1 = max([sum(x) for x in zip(*a)])
    normb = max(suma)
    suma2 = 0
    for i in range(n):
        for j in range(n):
            a[i][j] == a[i][j] ** 2
            suma2 += a[i][j]
    norme = sqrt(suma2)

    with open(resu, 'w', encoding="utf8") as f:
        f.write("Норма 1:\n")
        f.write(str(norm1))
        f.write("\nНорма 2:\n")
        f.write(str(norme))
        f.write("\nНескінчення норма:\n")
        f.write(str(normb))


# Виклик функції для 4 тестів
norm(file("Check1.txt"), "Result1.txt")
norm(file("Check2.txt"), "Result2.txt")
norm(file("Check3.txt"), "Result3.txt")
norm(file("Check4.txt"), "Result4.txt")

