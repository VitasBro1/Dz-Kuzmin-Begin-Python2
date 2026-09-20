N = int(input("Введите число N: "))
F1 = 1
F2 = 1
print("Числа:")
if N >= 1:
    print(f"F1 = {F1}")

if N >= 2:
    print(f"F2 = {F2}")

for c in range(3, N + 1):
    F_next = F1 + F2

print(f"F{c} = {F_next}")

F1 , F2 = F2 , F_next
