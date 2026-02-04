import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("dsm_data.csv")
t = data["t"]
x = data["x"]
v = data["v"]
a = data["a"]
E = data["E"]
b = data["b"]
k = data["k"]
m = data["m"]

plt.plot(t, x)
plt.title("x vs t")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.grid()
plt.show()

plt.plot(t,v)
plt.title("v vs t")
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
plt.grid()
plt.show()

plt.plot(t,E)
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


