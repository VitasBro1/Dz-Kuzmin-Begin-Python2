N = int(input("Введите число N: "))
num = 0.0

for c in range(1, N + 1):
    num += float(c) ** c

print(f"Сумма 1^1 + 2^2 + ... + {N}^{N} = {num}")
