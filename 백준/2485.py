import sys
import math

N = int(sys.stdin.readline())
gap = []

list_int = list(int(sys.stdin.readline().strip()) for i in range(N))
for i in range(1,N):
  gap.append(list_int[i] - list_int[i-1])

common_gcd = math.gcd(*gap)

print((list_int[-1] - list_int[0]) // common_gcd - (N-1))
