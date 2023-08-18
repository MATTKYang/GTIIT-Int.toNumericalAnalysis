import sympy as sp
from sympy.abc import x
def interpolate(points):
    P = 0
    for i in range(len(points)):
        L = 1
        for m in range(len(points)):
            if m != i:
                L = L * ((x - points[m][0]) / (points[i][0] - points[m][0])) # The formula 3.1
        P = sp.simplify((P + (points[i][1]) * L)) # The formula 3.2
    return (f'P(x) = {P}')
print(interpolate([[0,-1],[1,-0.5],[3,1],[4,2],[5,3]]))
