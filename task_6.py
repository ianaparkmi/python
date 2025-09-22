p=float(input("Введиет давление в паскалях:"))
v=float(input("Введиет объем в метрах:"))
T=float(input("Введиет температуру  в кельвинах:"))
R=8.31
n=(p*v)/(R*T)
print("result:", n)