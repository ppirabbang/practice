import sys

N, M = map(int, sys.stdin.readline().split())

list_int = [0] * N
for i in range(N):
    list_int[i] = i+1

temp = 0
for i in range(M):
    before,after = map(int, sys.stdin.readline().split())
    temp = list_int[before-1] 
    list_int[before-1] = list_int[after-1]
    list_int[after-1] = temp

for i in range(N):
    print(list_int[i], end=" ")