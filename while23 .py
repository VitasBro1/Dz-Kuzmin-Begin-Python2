A = int(input("Введите целое положительное число A: "))
B = int(input("Введите целое положительное число B: "))

while A <= 0 or B <= 0:
    print("Числа должны быть положительными!")
    A = int(input("Введите целое положительное число A: "))
    B = int(input("Введите целое положительное число B: "))

orig_A, orig_B = A, B

while B != 0:
    temp = B
    B = A % B
    A = temp

gcd = A
print(f"НОД({orig_A}, {orig_B}) = {gcd}")
