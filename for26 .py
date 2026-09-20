X = float(input("Введите число X (|X| < 1): "))
N = int(input("Введите число N: "))
m = 0.0
num = X  

for c in range(N + 1):
    if c > 0:
        num *= -X * X * (2 * c - 1) / (2 * c + 1)
    m += num

print(N , "+-" , m)
