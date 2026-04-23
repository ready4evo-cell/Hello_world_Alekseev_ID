array = [64, 34, 25, 12, 22, 11, 95]
n = len(array)
sum = 0
j = 1

for i in range(n):
        while j <= (n-1):
             sum = sum + array[j]
             j = j + 2

print(sum)