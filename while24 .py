N = int(input("Введите целое число N (> 1): "))

while N <= 1:
    N = int(input("Пожалуйста, введите N > 1: "))

F_prev = 1
F_curr = 1
is_fibonacci = False

if N == 1:
    is_fibonacci = True
else:
    while F_curr < N:
        F_next = F_prev + F_curr
        F_prev, F_curr = F_curr, F_next

    if F_curr == N:
        is_fibonacci = True

if is_fibonacci:
    print("TRUE")
else:
    print("FALSE")