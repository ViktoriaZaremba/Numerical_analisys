from math import log2
a = [1,1,0, 1]
b = bin(sum(a))
r = log2(len(a)+1)
print(b)
print(r)