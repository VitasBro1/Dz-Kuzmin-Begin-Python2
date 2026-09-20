one_kg = float(input("Введите цену 1 кг конфет: "))

for c in range(12, 22 , 2):
    delenie = round(c / 10, 1)
    ymnoch = round(one_kg * delenie,  2) 
    print(f"{delenie} кг конфет: {ymnoch} руб.")