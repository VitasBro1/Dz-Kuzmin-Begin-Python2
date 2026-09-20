N = int(input("Введите число N: "))
A1 = 1
A2 = 2
A3 = 3
print("Элементы:")
print(f"A1 = {A1}")
print(f"A2 = {A2}")
print(f"A3 = {A3}")

for c in range(4, N + 1):
    num = A3 + A2 - 2 * A1
    print(f"A{c} = {num}")

    A1, A2, A3 = A2, A3, num
