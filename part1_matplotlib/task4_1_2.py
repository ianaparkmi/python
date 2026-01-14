import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5/(x*x-9)

x1=np.linspace(-10,-3.1, 1000)
x2=np.linspace(-2.9, 2.9, 1000)
x3=np.linspace(3.1, 10, 1000)

plt.figure(figsize=(12,12))

plt.plot(x1,f(x1), color='green', linewidth=2)
plt.plot(x2,f(x2), color='blue', linewidth=2)
plt.plot(x3,f(x3), color='red', linewidth=2)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('graph of the function')
plt.grid(True)

plt.xlim(-10,10)
plt.ylim(-5,5)
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

plt.tight_layout()
plt.show()

