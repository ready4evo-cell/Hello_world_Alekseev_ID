array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)
sum = 0
j = 0
average = 0

for i in range(n):
            sum = sum + array[i]
            j = j+1
average=sum/j

print(average)