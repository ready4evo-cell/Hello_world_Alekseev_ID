height = float(input("Введите ваш рост (м): "))
weight = float(input("Введите ваш вес (кг): "))

bmi = weight / (height ** 2)
print("--- Отчет о состоянии здоровья ---")
print(f"Рост: {height}")
print(f"Вес: {weight}")
print(f"Индекс массы тела пациента: {bmi:.2f}")