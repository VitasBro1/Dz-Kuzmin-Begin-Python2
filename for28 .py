X = float(input("Введите число X (|X| < 1): "))
N = int(input("Введите число N: "))
m = 1.0 
n = 1.0  
num = 1.0 
sign = 1 

for c in range(1, N + 1):
    if c == 1:
        n = 1.0
    else:
        n *= (2 * c - 3)
    num *= 2 * c
    num2 = n / num * X ** c
    if c % 2 == 0: 
        num2 = -num2
    m += num2

print(N , "+-" , m)
