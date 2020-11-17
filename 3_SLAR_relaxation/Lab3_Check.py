import numpy as np

def file(f_name):
    f = open(f_name)
    sys = []
    for line in f:
        row = [float(i) for i in line.split()]
        sys.append(row)
    return sys

def check(sys):
    n = len(sys)
    a = []
    b = []
    for line in range(n-1):
        a.append(sys[line][0:-1])
        b.append(sys[line][-1])
    try:
        d = np.linalg.det(a)
        x = np.linalg.solve(a, b)
        print("Визначник:")
        print(d)
        print("Результат:")
        print(x)
    except np.linalg.LinAlgError as err:
        if 'Singular matrix' in str(err):
            print("Однозначного розв’язку немає")
        else:
            raise

print("Check1")
check(file("Check1.txt"))
print("\nCheck2")
check(file("Check2.txt"))
print("\nCheck3")
check(file("Check3.txt"))
print("\nCheck4")
check(file("Check4.txt"))
