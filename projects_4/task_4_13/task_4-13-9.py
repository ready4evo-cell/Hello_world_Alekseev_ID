array = [64, 34, 25, 12, 22, 11, 95]
n = len(array)
count = 0

for i in range(n):
   if array[i] % 2 != 0:
      count = count + 1

print(count)