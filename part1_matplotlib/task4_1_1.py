import numpy as np
import matplotlib.pyplot as plt
import math

x_degrees=np.linspace(-360,360,2000)
x_rad=np.radians(x_degrees)

def f1(x_rad):
    cos_x=np.cos(x_rad)
    cos_06x=np.cos(0.6*x_rad)**2
    return np.exp(cos_x)+ np.log(cos_06x + 1) * np.sin(x_rad)

def f2(x_rad):
    cos_x=np.cos(x_rad)
    sin_x=np.sin(x_rad)
    return - np.log((cos_x + sin_x)**2 + 2.5) + 10

plt.figure(figsize=(12, 8))
plt.plot(x_degrees,f1(x_rad), color='green', linewidth=2, label='f1(x)')
plt.plot(x_degrees,f2(x_rad), color='red', linewidth=2,label='f2(x)')


plt.xlabel("gradus")
plt.ylabel("Function values")
plt.title("Graphs of functions")
plt.grid(True)
plt.legend(fontsize=10)
plt.xlim(-360, 360) 

plt.xticks(np.arange(-360, 361, 90))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()
    