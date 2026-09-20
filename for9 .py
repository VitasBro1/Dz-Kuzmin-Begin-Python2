A = int(input("Введите A: "))
B = int(input("Введите B: "))
n = 1
for c in range(A , B + 1):
    n += c ** 2
    

print(f"Произведение равно: {A} do {B} = {n} " )