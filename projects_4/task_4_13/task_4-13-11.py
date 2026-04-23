array = [64, 34, 25, 12, 22, 11, 95]
n = len(array)
sum = 0
j = 0
count = 0

for i in range(n):
        while j <= (n-1):
             sum = sum + array[j]
             j = j + 2
             count = count + 1

print(sum/count)