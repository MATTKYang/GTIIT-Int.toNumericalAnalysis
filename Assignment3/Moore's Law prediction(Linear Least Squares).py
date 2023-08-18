import numpy as np
from sympy.abc import x
def Linear_LS(xs,ys):
    a_0 = a_1 = x_i = y_i = x_i2 = x_iy_i = 0
    for i in range(len(xs)):
        x_i2 += xs[i]**2
        y_i += ys[i]
        x_iy_i += xs[i] * ys[i]
        x_i += xs[i]
    a_0 = (x_i2 * y_i - x_iy_i * x_i) / (len(xs) * x_i2 - (x_i**2))
    a_1 = (len(xs) * x_iy_i - x_i * y_i) / (len(xs) * x_i2 - (x_i**2))
    P = a_0 + a_1 * x
    return(P)

data = np.loadtxt('moore.txt')
xs = data[:,0] # entire first column
ys = np.log10(data[:,1]) # In a logarithmic scale
print(Linear_LS(xs,ys))
print(10 ** Linear_LS(xs,ys).subs(x,2023))

