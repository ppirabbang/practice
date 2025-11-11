import sys

a = int(sys.stdin.readline().rstrip())
result = [0] * a
for i in range(a):
  b,c = map(int, sys.stdin.readline().split())
  result[i] = b + c

for i in range(a):
  print(result[i])