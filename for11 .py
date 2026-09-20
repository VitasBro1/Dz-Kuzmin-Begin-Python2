N = int(input("Введите число N: "))


sum = 0
for c in range(N, 2 * N + 1):
    sum += c ** 2


print(f"Сумма квадратов от {N}^2 до {2 * N}^2 равна: {sum}")
