N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

odd = []
count = 0
print(f"Введите {N} целых чисел:")

for i in range(N):
    number = int(input(f"Число {i + 1}: "))
    if number % 2 != 0:
        odd.append(i + 1)
        count += 1

print("\nНомера нечётных чисел в наборе:")

if odd:
    print(*odd)
else:
    print("Нечётных чисел нет")

print(f"Количество нечётных чисел: {count}")
