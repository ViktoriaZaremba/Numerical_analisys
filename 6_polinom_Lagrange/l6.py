import numpy as np
from math import sin
import matplotlib.pyplot as plt


def file(f_name):
    f = open(f_name)
    sys = []
    for line in f:
        row = [float(i) for i in line.split()]
        sys.append(row)
    return sys


x = np.array(file("check1.txt")[0])
y = np.zeros(x.size)
for i in range(x.size):
    y[i] = sin(np.array(file("check1.txt")[0])[i])


def lag(x1):
    res = 0
    for i in range(len(y)):
        del0 = 1
        delt = 1
        for j in range(len(x)):
            if i != j:
                del0 *= (x1-x[j])
                delt *= (x[i]-x[j])
        res += y[i]*del0/delt
    return res


inp_x = float(input())
if inp_x in x:
    for i in range(len(x)):
        if inp_x == x[i]:
            print(y[i])
else:
    print(lag(inp_x))


xnew = np.linspace(np.min(x),np.max(x),100)
ynew = [lag(i) for i in xnew]
plt.plot(x, y, "o", xnew, ynew)


time = np.arange(-1, 1, 0.2)
y_sin = np.sin(time)
plt.plot(time, y_sin)
plt.show()

a = 10
pog = np.linspace(np.min(x), np.max(x), a)
res_pog = np.zeros(a)
for i in range(10):
    m = np.sin(pog)
    n = lag(pog)
    res_pog[i] = m[i]-n[i]

print(max(res_pog))
