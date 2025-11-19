import sys

count = 0
list_int = [False] * 42
for i in range(10):
  a = int(sys.stdin.readline()) % 42
  list_int[a] = True
  
for i in range(42):
  if(list_int[i] == True):
    count += 1

print(count)