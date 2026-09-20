N = int(input("Введите число N: "))


n = 0.0
for c in range(N):
    m = (1.1 + c * 0.1) * (-1) ** c
    n += m


print(n)

