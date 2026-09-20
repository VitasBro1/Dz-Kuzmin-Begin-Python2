N = int(input("Введите целое число N (> 1): "))
K = 0
pow = 1

while pow <= N:
    pow *= 3
    K += 1
print(f"Наименьшее число K, при котором 3^K > {N}: {K}")
