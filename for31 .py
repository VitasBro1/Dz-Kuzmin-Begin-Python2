N = int(input("Введите число N: "))
m = 2.0
print("Элементы:")

for c in range(1, N + 1):
    n = 2 + 1 / m
    
    print("^" , c, "=", n)
    
    m = n

    
