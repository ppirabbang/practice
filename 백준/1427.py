import sys

N = int(sys.stdin.readline())
list_int = []

while(N > 0):
  list_int.append(N % 10)
  N = N // 10

list_int.sort(reverse=True)
for i in list_int:
  print(i, end="")