N = int(input("Введите целое число N (> 0): "))
count = 0
sum = 0

while N > 0:
    dig = N % 10
    sum += dig
    count += 1
    N = N // 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {sum}")
