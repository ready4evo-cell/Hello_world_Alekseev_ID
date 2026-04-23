n = int(input("Введите числа N: "))
i = 1
k = 0
sum = 0

while i <= n: 
    k = i*i
    sum = sum + k
    i = i + 1

print(sum)