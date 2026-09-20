A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

print("Числа в диапазоне от A до B:")
current = A
count = 0
while current <= B:
    print(current, end=" ")
    count += 1
    current += 1
print(f"\nКоличество чисел в диапазоне: {count}")
