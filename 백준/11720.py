import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()
sum = 0
  
for i in range(a):
  sum += int(b[i])

print(sum)