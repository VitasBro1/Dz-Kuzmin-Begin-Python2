N = int(input("Введите целое число N (> 0): "))
num = 0

while N > 0:
    digit = N % 10
    num = num * 10 + digit
    N = N // 10

print(f"Число, полученное при прочтении справа налево: {num}")
