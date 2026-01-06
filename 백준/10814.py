import sys

N = int(sys.stdin.readline())

list_info = []

for i in range(N):
  age,name = sys.stdin.readline().split()
  list_info.append([int(age),name])

list_info.sort(key=lambda x : x[0])

for i in list_info:
  print(i[0], i[1])