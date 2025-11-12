import sys

a = int(sys.stdin.readline())

list_sum = [0] * a
list_b = [0] * a
list_c = [0] * a
for i in range(a):
  b, c = map(int, sys.stdin.readline().split())
  list_b[i] = b
  list_c[i] = c
  list_sum[i] = b + c

for i in range(a):
  print(f"Case #{(i+1)}: {list_b[i]} + {list_c[i]} = {list_sum[i]}")