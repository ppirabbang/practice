import sys

a = int(sys.stdin.readline())
list_int  = list(map(int, sys.stdin.readline().split()))

b = int(sys.stdin.readline())
count = 0
for i in list_int:
  if b == i:
    count += 1

print(count)