import numpy as np

def rectangle_method(f, a, b, n=1000):
    dx = (b - a) / n
    x = np.linspace(a, b - dx, n)
    return np.sum(f(x)) * dx

def double_integral_rectangle(f, x_limits, y_limits, nx=100, ny=100):
    a, b = x_limits
    c, d = y_limits
    dx = (b - a) / nx
    dy = (d - c) / ny
    x = np.linspace(a, b - dx, nx)
    y = np.linspace(c, d - dy, ny)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    return np.sum(Z) * dx * dy

def f1(x):
    return x**2 + 2*x + 1

a, b = 0, 2
result_definite = rectangle_method(f1, a, b)
print(f"Definite integral of (x^2 + 2x + 1) from {a} to {b}")
print(f"Result: {result_definite:.4f}")

def f2(x, y):
    return x**2 + y**2

x_limits = (0, 1)
y_limits = (0, 1)
result_double = double_integral_rectangle(f2, x_limits, y_limits)
print(f"\nDouble integral of (x^2 + y^2), x from {x_limits[0]} to {x_limits[1]}, y from {y_limits[0]} to {y_limits[1]}")
print(f"Result: {result_double:.4f}")