sum = 0.0
print("Введите 10 вещественных чисел:")

for c in range(10):
    num = float(input(f"Число {c + 1}: "))
    sum += num

aver = sum / 10
print(f"\nСреднее арифметическое десяти чисел: {aver}")
