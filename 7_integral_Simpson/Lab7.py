a =float(input())
b =float(input())
n =int(input())
def fun(x):
    return ((x + 3.8)**3)/(3.3 * x*x + 5.5*x + 2.2)

h=(b-a)/(2*n)

s=fun(a)-fun(b)

e=1
n_fin=1
eps =0.000005
prom=0
i = 1
print(s-prom)
while((s-prom)>eps):
    prom=s
    s=s+(3+e)*fun(a+i*h)
    e=e*(-1)
    n_fin+=1
    i+=1
s=s*h/3

print(s)
print(n_fin)

