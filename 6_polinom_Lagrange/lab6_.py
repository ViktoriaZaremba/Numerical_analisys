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
y = np.array(file("check1.txt")[1])


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

plt.show()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)


