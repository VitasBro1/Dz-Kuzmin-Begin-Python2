X = float(input("Введите число X: "))
N = int(input("Введите число N: "))
m = 1.0  
sum= 1.0  

for c in range(1, N + 1):
    sum *= -X * X / ((2 * c - 1) * (2 * c))
    m += sum

print(X , "+-" , m)
