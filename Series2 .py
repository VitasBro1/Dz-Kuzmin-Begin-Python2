prod = 1.0
print("Введите 10 вещественных чисел:")

for c in range(10):
    num = float(input(f"Число {c + 1}: "))
    prod *= num

print(f"\nПроизведение десяти чисел: {prod}")
