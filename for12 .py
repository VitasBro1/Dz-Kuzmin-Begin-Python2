N = int(input("Введите число N: "))


m = 1.0
n = 1.1

for c in range(N):
    m *= n
    n += 0.1

print(m)
