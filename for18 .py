A = float(input("Введите число A: "))
N = int(input("Введите число N: "))


m = 1.0  
n = 1.0  


for c in range(1, N + 1):
    n *= -A  
    m += n

print(m)

