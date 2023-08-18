import numpy as np
import matplotlib.pyplot as plt

def RK4_step(func, dt, tk, wk):
    K1 = dt * func(tk, wk)
    K2 = dt * func(tk + dt / 2, wk + K1 / 2)
    K3 = dt * func(tk + dt / 2, wk + K2 / 2)
    K4 = dt * func(tk + dt, wk + K3)

    w = wk + (K1 + 2 * K2 + 2 * K3 + K4)/6 # This w is w_k+1.
    t = tk + dt  # This t is t_k+1.
    return(t,w)

def lorenz(t,w):
    x,y,z = w
    return np.array([10 * (y - x), x * (28 - z) - y, x * y - (8/3) * z])

w0 = np.array([-8, 7, 25])
w00 = np.array([-4, 5, 30])
dt = 0.01
t = 0
total_solution_time = np.arange(0.0, 6.0, dt)
# We choose time = 6 here.
state1 = []
state2 = []
wk1 = w0
wk2 = w00
for i in total_solution_time:
    state1.append(wk1)
    wk1 = RK4_step(lorenz, 0.01, i, wk1)[1]
state1 = np.array(state1)

for j in total_solution_time:
    state2.append(wk2)
    wk2 = RK4_step(lorenz, 0.01, j, wk2)[1]
state2 = np.array(state2)

# Create figure and 3D axes:
fig = plt.figure()
ax = plt.axes(projection='3d')
x_data1 = []
y_data1 = []
z_data1 = []
x_data2 = []
y_data2 = []
z_data2 = []

for m in range(len(state1)):
    x_data1.append(state1[m][0])
    y_data1.append(state1[m][1])
    z_data1.append(state1[m][2])

for n in range(len(state2)):
    x_data2.append(state2[n][0])
    y_data2.append(state2[n][1])
    z_data2.append(state2[n][2])

# Add the plots:
ax.plot3D(x_data1, y_data1, z_data1, 'b', label="Initial states (x0,y0,z0) = (-8,7,25)",markersize=1)
ax.plot3D(x_data2, y_data2, z_data2, 'r', label="Initial states (x0,y0,z0) = (-4,5,30)",markersize=1)
plt.title("The Lorenz Attractor for total solution time = 6")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.legend()
plt.show()


