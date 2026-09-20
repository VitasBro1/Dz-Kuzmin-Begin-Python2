N = int(input("Введите целое положительное число N: "))
K = int(input("Введите целое положительное число K: "))
quo = 0
rem= N
while rem>= K:
    rem -= K
    quo += 1

print(f"Частное от деления N на K: {quo}")
print(f"Остаток от деления N на K: {rem}")
