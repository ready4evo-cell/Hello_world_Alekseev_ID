fio=input("ФИО: ")
date=input("Дата: ")
exp_name=input("Эксперимент: ")
conclusion=input("Вывод: ")
with open("journal.txt", "w", encoding="utf-8") as recipe:
    
    recipe.write("+--------------------------------------------------+\n|        Электронный лабораторный журнал           |\n+--------------------------------------------------+\n")
    recipe.write(f"| ФИО исследователя: {fio}          |\n")
    recipe.write(f"| Дата: {date}                                 |\n")
    recipe.write(f"| Название: {exp_name}              |\n")
    recipe.write("+--------------------------------------------------+\n")
    recipe.write(f"| Вывод: {conclusion}                     |\n")
    recipe.write("+--------------------------------------------------+")

