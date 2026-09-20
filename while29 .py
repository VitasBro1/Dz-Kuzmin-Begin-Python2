epsilon = float(input("Введите вещественное число ε (> 0): "))

while epsilon <= 0:
    epsilon = float(input("Пожалуйста, введите ε > 0: "))
A_prev = 1.0
A_curr = 2.0
K = 2

while True:
    A_next = (A_prev + 2 * A_curr) / 3

    if abs(A_next - A_curr) < epsilon:
        break

    A_prev, A_curr = A_curr, A_next
    K += 1
print(f"Номер K: {K + 1}")
print(f"A_{K}: {A_curr}")
print(f"A_{K+1}: {A_next}")
