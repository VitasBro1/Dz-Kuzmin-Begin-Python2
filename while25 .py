N = int(input("Введите целое число N (> 1): "))

while N <= 1:
    N = int(input("Пожалуйста, введите N > 1: "))
prev = 1
curr = 1

while curr <= N:
    next = prev + curr
    prev, curr = curr, next

print(f"Первое число Фибоначчи, большее {N}: {curr}")
