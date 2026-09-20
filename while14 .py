A = float(input("Введите число A (> 1): "))
K = 1
sum = 1.0
sum3 = 0.0

while sum < A:
    sum3= sum 
    K += 1
    sum += 1 / K

if sum >= A:
    K -= 1

    sum2 = sum3
else:
    sum2 = sum

print(f"Наибольшее число K: {K}")
print(f"Сумма 1 + 1/2 + ... + 1/K: {sum2}")
