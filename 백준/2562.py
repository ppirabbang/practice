import sys

list_int = [0] * 9
for i in range(9):
  list_int[i] = int(sys.stdin.readline())

maximum = max(list_int)
index = 0
for i in range(9):
  if (maximum == list_int[i]):
    index += (i+1)

print(maximum)
print(index)