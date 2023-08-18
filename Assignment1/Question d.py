import math
list = []
def bisection(a,b,func,tol):
    if func(a) * func(b) < 0: #The interval should satisfy the Intermediate Value Theorem 
        i = 1
        FA = func(a)
        while True:
            p = a + (b - a)/2
            list.append(p)
            FP = func(p)
            if FP == 0 or (b - a)/2 < tol: #Here to jump out the loop
                print(list)
                print(f'The number of iteration is {i}')
                print(f'The approximation x = {p}')
                return
            i += 1
            if FA * FP > 0:
                a = p
                FA = FP
            else:
                b = p
    else:
        return ("Can not use the Bisection Method!")



def func_d(x):
    func_d = x**6 + 6*x**5 + 9*x**4 -2*x**3 - 6*x**2 +1
    return func_d


print(bisection(-3,-2,func_d,10**-5))
