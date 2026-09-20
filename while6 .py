N = int(input("Введите целое число N (> 0): "))
res = 1.0
cur = N

while cur > 0:
    res *= cur
    cur -= 2

print(f"Двойной факториал {N}!! = {res}")
