A = int(input("Введите положительное число A: "))
B = int(input("Введите положительное число B: "))
C = int(input("Введите положительное число C: "))

while A <= 0 or B <= 0 or C <= 0:
    print("Все числа должны быть положительными!")
    A = int(input("Введите положительное число A: "))
    B = int(input("Введите положительное число B: "))
    C = int(input("Введите положительное число C: "))

count_horizontal = 0
temp_A = A
while temp_A >= C:
    temp_A -= C
    count_horizontal += 1

count_vertical = 0
temp_B = B
while temp_B >= C:
    temp_B -= C
    count_vertical += 1

total_squares = 0
for _ in range(count_vertical):
    total_squares += count_horizontal
print(f"Количество квадратов, размещённых на прямоугольнике: {total_squares}")
