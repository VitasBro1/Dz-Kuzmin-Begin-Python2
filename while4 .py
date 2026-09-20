N = int(input("Введите целое число N (> 0): "))
orig_N = N

while N % 3 == 0:
    N = N // 3

if N == 1:
    print("TRUE")
else:
    print("FALSE")
