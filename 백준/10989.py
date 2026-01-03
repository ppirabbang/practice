import sys

N = int(sys.stdin.readline())
list_int = [0] * 10001

for _ in range(N):
  num = int(sys.stdin.readline())
  list_int[num] += 1

for i in range(10001):
  if(list_int[i] != 0):
    for _ in range(list_int[i]):
      print(i)