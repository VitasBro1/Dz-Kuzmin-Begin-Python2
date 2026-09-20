N = int(input("Введите число N: "))
A = float(input("Введите точку A: "))
B = float(input("Введите точку B: "))
H = (B - A) / N
print(f"Длина H = {H}")
print("Точки разбиения:")

for c in range(N + 1):
    num = A + c * H
    print(f"A + {c}·H = {num}")
