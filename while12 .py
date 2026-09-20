N = int(input("Введите целое число N (> 1): "))
K = 0
sum = 0

while sum + (K + 1) <= N:
    K += 1
    sum += K 

print(f"Наибольшее число K: {K}")
print(f"Сумма 1 + 2 + ... + K: {sum}")
