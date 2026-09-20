N = int(input("Введите целое число N (> 1), являющееся числом Фибоначчи: "))

while N <= 1:
    N = int(input("Пожалуйста, введите N > 1: "))
F_prev = 1
F_curr = 1

if N == 1:
    F_prev_fib = 0
    F_next_fib = 2
else:
    while F_curr < N:
        F_next = F_prev + F_curr
        F_prev, F_curr = F_curr, F_next

    F_prev_fib = F_prev
    F_next_fib = F_curr + F_prev

print(f"Предыдущее число Фибоначчи: {F_prev_fib}")
print(f"Следующее число Фибоначчи: {F_next_fib}")
