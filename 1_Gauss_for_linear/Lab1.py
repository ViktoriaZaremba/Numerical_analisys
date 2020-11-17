def file(f_name):
    #зчитує файл з елементами СЛАР та записує інформацію у матрицю  sys
    #f_name - назва файлу
    f = open(f_name)
    sys = []
    for line in f:
        row = [float(i) for i in line.split()]
        sys.append(row)
    return sys

def gaus(a, resu):
    #функція для обчислення результату розв'язанняСЛАР методом Гауса
    #a - matrix
    #resu - назва файлу, у який записується результат
    n = len(a)
    x = [0]*n
    count = 0
    #прямий хід
    for k in range(n - 1):  # 1
        swap(a, k, resu)
        for i in range(k+1, n):#2
            m = -(a[i][k]/a[k][k]) #3
            a[i][-1] = a[i][-1] + m * a[k][-1] #4
            for j in range(k+1, n): #5
                a[i][j] = a[i][j] + m*a[k][j] #6
                count += 1

    #Перевірка на наявність однозначного розв'язку
    for i in range(len(a)):
        if a[i][i]==0:
            with open(resu, 'w', encoding="utf8") as f:
                f.write("Однозначного розв’язку немає")
                f.write("\nВизначник = 0")
            return

    #зворотній хід
    for k in range(n-1, -1, -1): #8
        x[k] = (a[k][-1] - sum([a[k][j] * x[j] for j in range(k+1, n)])) / a[k][k] #9

    #визначник
    det = 1
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                det = det * a[i][j]
    det = - pow(-1, count) * det

    #запис результатів у файл
    with open(resu, 'w', encoding="utf8") as f:
        f.write("Визначник:\n")
        f.write(str(det))
        f.write("\n\nРезультат:\n")
        for item in x:
            f.write(" %s\n" % item)
    return x

def swap(a, col, resu):
    # шукає максимальний елемент стовпця і міняє місця рядки матриці
    #a - matrix
    #col - індекс стовпця, в якому шукаєм
    #resu - назва файлу, в який заисується результат, в разі необхідності
    maxe = a[col][col]
    maxr = col
    for q in range(col+1, len(a)):
        if abs(a[q][col]) > abs(maxe):
            maxe = a[q][col]
            maxr = q
        if abs(maxe) <= 0.0001:
            with open(resu, 'w', encoding="utf8") as f:
                f.write("Однозначного розв’язку немає")
                f.write("\nВизначник = 0")
    if maxr != col:
        a[col], a[maxr] = a[maxr], a[col]

#Виклик функції для 4 тестів
#gaus(file("Check1.txt"), "Result1_1.txt")
#gaus(file("Check2.txt"), "Result1_2.txt")
#gaus(file("Check3.txt"), "Result1_3.txt")
gaus(file("Check4.txt"), "Result1_4.txt")
