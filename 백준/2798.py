import sys

N, M = map(int, sys.stdin.readline().split())
list_ = list(map(int,sys.stdin.readline().split()))
max = 0


for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if(list_[i]+list_[j]+list_[k] <= M and max < list_[i]+list_[j]+list_[k]):
        max = list_[i]+list_[j]+list_[k]

print(max)