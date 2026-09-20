X = float(input("Введите число X: "))
N = int(input("Введите число N: "))
m = 0.0
num_1 = X
num_2 = 1

for c in range(1, N + 1):
    if c > 1:
        num_1 *= X / c
        num_2 *= -1
        num_3 = num_2 * abs(num_1)
    else:
        num_3 = num_1
    m += num_3

print(f"(1 + {X}) +- {m}")
