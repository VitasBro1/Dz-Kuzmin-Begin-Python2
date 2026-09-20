A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print("Результат:")

for c in range(A, B + 1):
    count = c - A + 1
    print((str(c) + " ") * count)
