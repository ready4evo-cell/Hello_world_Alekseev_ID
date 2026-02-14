general_volume=float(input("Общий объём: "))
salt_mass=general_volume*0.009
with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\n")
    recipe.write(f"Общий объем: {general_volume} мл\n")
    recipe.write(f"Масса соли: {salt_mass:.2f} г\n")
    recipe.write(f"Объём воды: {general_volume} мл\n")
