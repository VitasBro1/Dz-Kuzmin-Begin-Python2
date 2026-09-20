N = int(input("Введите число N: "))
one_n= 0

print("Квадраты чисел от 1 до", N, ":")
for c in range(1, N + 1):
    two_n = 2 * c - 1  
    one_n += two_n  
    print(f"{c}^2 = {one_n}")  
