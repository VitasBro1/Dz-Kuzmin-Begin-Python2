N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

sum = 0.0
prod = 1.0
print(f"Введите {N} вещественных чисел:")

for c in range(N):
    num = float(input(f"Число {c + 1}: "))
    sum += num
    prod *= num

print(f"\nСумма чисел: {sum}")
print(f"Произведение чисел: {prod}")
