N = int(input("Введите число N: "))
A1 = 1.0
A2 = 2.0

print("Элементы:")
print(f"A1 = {A1}")

if N >= 2:
    print(f"A2 = {A2}")

for c in range(3, N + 1):
    m = (A1 + 2 * A2) / 3
    print(f"A{c} = {m}")
    A1, A2 = A2, m
