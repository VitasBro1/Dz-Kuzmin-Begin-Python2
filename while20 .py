N = int(input("Введите целое число N (> 0): "))
found = False

while N > 0:
    digit = N % 10
    if digit == 2:
        found = True
        break
    N = N // 10

if found:
    print("TRUE")
else:
    print("FALSE")
