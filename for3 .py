A = int(input("Введите A: "))
B = int(input("Введите B(B > A): "))

for c in range(B - 1 , A, - 1):
    print (c)

N = B - A - 1
print(f"N: {N} ")