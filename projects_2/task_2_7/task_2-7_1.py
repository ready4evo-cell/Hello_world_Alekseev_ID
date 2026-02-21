files = ["Образец _1 ", "Образец_2 ", "Образец_3 ", "Образец_4 "]
date=input("Введите дату: ")
for name in files:
   new_name = name + date
   print(f"{new_name}")