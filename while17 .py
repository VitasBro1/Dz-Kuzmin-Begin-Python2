N = int(input("Введите целое число N (> 0): "))

while N > 0:
    digit = N % 10
    print(digit)
    N = N // 10
