from sympy import diff
from sympy.abc import x
def newton(p0,f,tol,max_iter):
    df = diff(f,x)# This is f'(x).
    ddf = diff(diff(f,x))# This is f''(x).
    p = p0
    p_temp = 0
    num_iter = 1
    while num_iter <= max_iter: # Here to test if it's smaller than the max iteration.
        if abs(p - p_temp) < tol:
            return (f'The root is {p}.The number of iterations is {num_iter}.')
        else:
            p_temp = p
            p = p - ((f.subs(x,p)*df.subs(x,p))/((df.subs(x,p)**2)-f.subs(x,p)*ddf.subs(x,p)))
            # p is the equation in 2.13
            num_iter += 1
    return(f'The method failed after {max_iter} iterations.')
f = -0.00416666666666667*x**4 + 0.0333333333333333*x**3+ 0.00416666666666714*x**2 + 0.466666666666666*x - 1.0
print(newton(-1,f,10**(-5),100))
print(newton(3,f,10**(-5),100))
print(newton(5,f,10**(-5),100))
print(newton(7,f,10**(-5),100))
print(newton(11,f,10**(-5),100))