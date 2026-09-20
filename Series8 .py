N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

even = []
count_even = 0
print(f"Введите {N} целых чисел:")

for c in range(N):
    num = int(input(f"Число {c + 1}: "))

    if num % 2 == 0:
        even.append(num)
        count_even += 1

print("\nЧётные числа из набора:")

if even:
    print(*even)
else:
    print("Чётных чисел нет")

print(f"Количество чётных чисел: {count_even}")
