import sys

a = int(sys.stdin.readline())
list_string = [""] * a

for i in range(a):
  b = sys.stdin.readline().rstrip()
  list_string[i] = b[0] + b[-1]

for i in range(a):
  print(list_string[i])