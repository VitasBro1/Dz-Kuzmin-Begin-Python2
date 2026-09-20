N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

prod = 1.0
print(f"Введите {N} положительных вещественных чисел:")

for i in range(N):
    number = float(input(f"Число {i + 1}: "))
    part = number - int(number)
    print(f"Дробная часть числа {number}: {part}")
    prod *= part

print(f"\nПроизведение всех дробных частей: {prod}")
