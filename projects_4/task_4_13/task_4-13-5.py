numbers = [float(i) for i in input("Введите числа через пробел: ").split()]
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("Среднее арифметическое:", average)
