p=float(input("Введите давление в паскалях:"))
v=float(input("Введите объем в метрах:"))
T=float(input("Введите температуру  в кельвинах:"))
R=8.31
n=(p*v)/(R*T)
print("result:", n)