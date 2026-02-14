operator=input("Имя оператора: ")
bar_count=input("Текущее значение давления (Па): ")
with open("sensor_log.txt", "w", encoding="utf-8") as list:
    
    list.write(f"ОПЕРАТОР\t\tЗНАЧЕНИЕ\n{operator}\t\t{bar_count}")

print("Данные успешно сохранены в sensor_log.txt")