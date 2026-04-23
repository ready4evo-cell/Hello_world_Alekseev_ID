x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))
a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
min = 0

if x > y: min = y
else: min = x
if min > a: min = a
elif min > b: min = b

print(min)