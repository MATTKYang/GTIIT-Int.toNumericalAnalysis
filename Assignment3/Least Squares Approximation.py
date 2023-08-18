import numpy as np
from sympy.abc import x
def LS(xs,ys,degree):
    A = []
    B = []
    tmp_list = []
    tmp_num1 = tmp_num2 = P = E = 0

    for i in range(degree+1):
        for j in range(degree+1):
            for k in range(0,len(xs)):
                tmp_num1 += xs[k] ** (j+i)
                tmp_num2 += ys[k] * (xs[k] ** (j + i))
            tmp_list.append(tmp_num1)
            tmp_num1 = 0
            if len(B) == degree+1:
                continue
            else:
                B.append(tmp_num2)
                tmp_num2 = 0
        A.append(tmp_list)
        tmp_list = []
    print(A)
    print(B)
    result = np.linalg.inv(np.array(A)).dot(np.array(B))
    # The above code finds the n-array with the coefficients of the polynomial.

    for m in range(len(result)):
        P += result[m] * (x**m) # This is the least square polynomial P(x).
    for n in range(len(xs)):
        E += (ys[n] - P.subs(x,xs[n]))**2 # This is the error.

    return(f"When degree = {degree}, the n-array with the coefficients of the polynomial is: {result}, and the error is {E}")

data = np.loadtxt('data_points.txt')
xs = data[:,0] # entire first column
ys = data[:,1] # entire second column

print(LS(xs,ys,1))
print(LS(xs,ys,2))
print(LS(xs,ys,3))