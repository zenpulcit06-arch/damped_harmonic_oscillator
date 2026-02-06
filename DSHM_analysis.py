import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("dsm_data.csv")
t = data["t"]
x = data["x"]
v = data["v"]
a = data["a"]
E = data["E"]
b = data["b"]
k = data["k"]
m = data["m"]

E0 = E[0]
mask = (E > 0) & (E > 0.05 * E0)
v0 = v[0]
k = k[0]
m = m[0]

t_fit = t[mask]
E_fit = E[mask]

plt.plot(t, x)
plt.title("x vs t")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.grid()
plt.show()

plt.plot(t, v)
plt.title("v vs t")
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
plt.grid()
plt.show()

plt.plot(t, E)
plt.title("E vs t")
plt.xlabel("Time(s)")
plt.ylabel("Energy(J)")
plt.grid()
plt.show()

plt.plot(x, v)
plt.title("Phase - Space analysis")
plt.xlabel("Position(m)")
plt.ylabel("Velocity(m/s)")
plt.grid()
plt.show()

slope, intercept = np.polyfit(t_fit, np.log(E_fit), 1)
d_const = -slope / 2

print(f"damping constant = {d_const:.2f}")

d_coff = 2 * m * d_const
print(f"damping cofficiant = {d_coff:.2f}")

angular_f_ana = np.sqrt((k / m) - (d_coff / (2 * m)) ** 2)

angular_f_th = np.sqrt((k / m) - (b.iloc[0] / (2 * m)) ** 2)


print(f"Theoretical omega = {angular_f_th}")
print(f"Analytical omega = {angular_f_ana}")

damped_term = (b.iloc[0] / (2 * m)) ** 2
natural_term = k / m

if damped_term > natural_term:
    print("This is over damped oscillation")
elif damped_term < natural_term:
    print("This is under damped oscillation")
else:
    print("This is criticaly damped oscillation")
