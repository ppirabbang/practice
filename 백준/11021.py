import sys

a = int(sys.stdin.readline())

list = [0] * a
for i in range(a):
  b, c = map(int, sys.stdin.readline().split())
  list[i] = b + c

for i in range(a):
  print("Case #" ,(i+1) , ": " , list[i])