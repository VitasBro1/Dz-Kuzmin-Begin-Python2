one_kg = float(input("Введите цену 1 кг конфет: "))

for c in range(1, 11):
    delenie = round(c / 10, 1)  # явное округление до 1 знака после запятой
    ymnoch = round(one_kg * delenie,  2)  # округление стоимости до копеек
    print(f"{delenie} кг конфет: {ymnoch} руб.")

