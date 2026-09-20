N = int(input("Введите целое число N (> 0): "))

while N <= 0:
    N = int(input("Пожалуйста, введите N > 0: "))

has = False
print(f"Введите {N} целых чисел:")

for c in range(N):
    number = int(input(f"Число {c + 1}: "))
    if number > 0:
        has = True
        break

if has:
    print("TRUE")
else:
    print("FALSE")
