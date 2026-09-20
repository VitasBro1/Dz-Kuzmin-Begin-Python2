N = int(input("Введите число N: "))
m = 1.0


print("Элементы:")
for c in range(1, N + 1):
    num = (m + 1) / c
    
    print(f"A{c} = {num}")
    
    m = num
