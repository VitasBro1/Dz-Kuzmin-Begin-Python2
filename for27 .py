X = float(input("Введите число X (|X| < 1): "))
N = int(input("Введите число N: "))
m = 0.0
n = X 
num = 1  

for c in range(N + 1):
    if c > 0:
        n *= (2 * c - 1) * X * X
        num *= 2 * c * (2 * c + 1)
    m += n / num

print(X , "+-" , m)
