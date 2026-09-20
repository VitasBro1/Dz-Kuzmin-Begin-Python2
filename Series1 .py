total_sum = 0.0
print("Введите 10 вещественных чисел:")

for c in range(10):
    number = float(input(f"Число {c + 1}: "))
    total_sum += number

print(f"\nСумма десяти чисел: {total_sum}")
