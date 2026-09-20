P = float(input("Введите процент увеличения пробега P (0 < P < 50): "))

while P <= 0 or P >= 50:
    P = float(input("Пожалуйста, введите P в диапазоне 0 < P < 50: "))

cur = 10.0
tot = 10.0
K = 1

while tot <= 200:
    cur += cur * P / 100
    tot += cur
    K += 1

print(f"Количество дней K: {K}")
print(f"Суммарный пробег S: {tot} км")
