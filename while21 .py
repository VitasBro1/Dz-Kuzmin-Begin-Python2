N = int(input("Введите целое число N (> 0): "))
has = False

while N > 0:
    digit = N % 10
    if digit % 2 != 0:
        has = True
        break 
    N = N // 10

if has:
    print("TRUE")
else:
    print("FALSE")
