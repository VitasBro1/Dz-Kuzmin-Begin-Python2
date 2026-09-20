A = float(input("Введите число A (> 1): "))
K = 1
sum = 1.0

while sum <= A:
    K += 1
    sum += 1 / K

print(f"Наименьшее число K: {K}")
print(f"Сумма 1 + 1/2 + ... + 1/K: {sum}")
