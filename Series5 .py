N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

sum_of_integers = 0.0
print(f"Введите {N} положительных вещественных чисел:")

for i in range(N):
    number = float(input(f"Число {i + 1}: "))
    integer = int(number)
    print(f"Целая часть числа {number}: {float(integer)}")
    sum_of_integers += integer

print(f"\nСумма всех целых частей: {sum_of_integers}")

