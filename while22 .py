N = int(input("Введите целое число N (> 1): "))

while N <= 1:
    N = int(input("Пожалуйста, введите N > 1: "))

prime = True
divi = 2

while divi * divi <= N:
    if N % divi == 0:
        prime = False
        break
    divi += 1

if prime:
    print("TRUE")
else:
    print("FALSE")
