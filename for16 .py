A = float(input("Введите число A: "))
N = int(input("Введите число N: "))


for c in range(1, N + 1):
    b = A ** c
    print(f"A^{c} = {b}")
