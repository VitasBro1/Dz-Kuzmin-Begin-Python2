import math

N = int(input("Введите число N: "))
A = float(input("Введите точку A: "))
B = float(input("Введите точку B: "))
H = (B - A) / N
print(f"Длина H = {H}")
print("F(X) = 1 - sin(X):")

for c in range(N + 1):
    x = A + c * H
    F = 1 - math.sin(x)
    print(f"F({x}) = {F}")
