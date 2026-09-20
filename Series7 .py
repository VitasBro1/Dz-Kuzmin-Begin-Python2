N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

sum_rounded = 0
print(f"Введите {N} вещественных чисел:")

for i in range(N):
    number = float(input(f"Число {i + 1}: "))
    rounded = round(number)
    print(f"Округлённое значение числа {number}: {rounded}")
    sum_rounded += rounded

print(f"\nСумма всех округлённых значений: {sum_rounded}")
