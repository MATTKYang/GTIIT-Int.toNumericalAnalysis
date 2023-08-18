import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('data_points.txt')
x_data = data[:,0] # entire first column
y_data = data[:,1] # entire second column

def p1(x):
    return 0.528102053515867 * x + 0.929514042729724

def p2(x):
    return 1.14733030545859 * x**2 - 0.325698750708621 * x + 1.01134099279321

def p3(x):
    return 1.02102256421131 * x**3 - 0.0115056745189577 * x**2 - 0.00154098604718911 * x + 1.00043980518403

x_values = np.linspace(0, 1.05, 500)

plt.plot(x_data, y_data,'r.', label="Data points",markersize=10)
plt.plot(x_values, p1(x_values), label="degree = 1")
plt.plot(x_values, p2(x_values), label="degree = 2")
plt.plot(x_values, p3(x_values), label="degree = 3")

plt.title("Data points and polynomials")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.grid()
plt.show()
