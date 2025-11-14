import numpy as np

A=np.array([[-2,-8.5,-3.4, 3.5],
           [0, 2.4, 0, 8.2],
           [2.5,1.6, 2.1, 3],
           [0.3, -0.4, -4.8, 4.6]])

B=np.array([-1.88, -3.28, -0.5, -2.83])
print(f"Определитель матрицы A: {np.linalg.det(A)}")
if np.linalg.det(A) == 0:
    print("матрица вырождена, нет решений")
else:
    A_inv=np.linalg.inv(A)
    X=A_inv @ B

    print("Решение системы:")
    print(f"x1 = {X[0]:.1f}")
    print(f"x2 = {X[1]:.1f}")
    print(f"x3 = {X[2]:.1f}")
    print(f"x4 = {X[3]:.1f}")
