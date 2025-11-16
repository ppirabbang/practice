import sys

a = int(sys.stdin.readline())

list_int = list(map(int,sys.stdin.readline().split()))
max = list_int[0]
min = list_int[0]

for i in list_int:
  if(i > max):
    max = i
  elif(i < min):
    min = i
print(min,max, end=" ")