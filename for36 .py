N = int(input("Введите число N: "))
K = int(input("Введите число K: "))
num = 0.0

for c in range(1, N + 1):
    num += float(c) ** K

print(f"Сумма 1^{K} + 2^{K} + ... + {N}^{K} = {num}")
