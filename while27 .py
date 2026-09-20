N = int(input("Введите целое число N (> 1), являющееся числом Фибоначчи: "))

while N <= 1:
    N = int(input("Пожалуйста, введите N > 1: "))
F_prev = 1
F_curr = 1
K = 2

if N == 1:
    K = 1
else:
    while F_curr < N:
        F_next = F_prev + F_curr
        F_prev, F_curr = F_curr, F_next
        K += 1
print(f"Порядковый номер числа Фибоначчи {N}: {K}")
