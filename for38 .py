N = int(input("Введите число N: "))
num = 0.0

for c in range(1, N + 1):
    num2 = N - c + 1
    num3 = float(c) ** num2
    num += num3

print(f"Сумма 1^{N} + 2^{N-1} + ... + {N}^1 = {num}")
