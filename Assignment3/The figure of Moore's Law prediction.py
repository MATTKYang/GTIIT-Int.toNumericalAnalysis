import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('moore.txt')
x_data = data[:,0]
y_data = np.log10(data[:,1])

def p(x):
    return 0.154018179843825*x - 300.290221658514

x_values = np.linspace(1971, 2030, 20000)

plt.title("1e10", loc="left")
plt.plot(x_data, y_data,'r.', label="Data points",markersize=10)
plt.plot(x_values, p(x_values), label="0.154018179843825x - 300.290221658514")
plt.xlabel("Year")
plt.ylabel("Transistors")
plt.title("Raw data and Model")
plt.legend()
plt.grid()
plt.show()
