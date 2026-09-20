A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (> 0): "))


n = 1.0
for c in range(N):
    n *= A

print(n)
