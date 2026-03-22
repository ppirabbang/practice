import sys

n = int(sys.stdin.readline())
cost = []


for i in range(n):
  cost.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      cost[i][j] += cost[i-1][j]
    elif(j == i):
      cost[i][j] += cost[i-1][j-1]
    else:
      cost[i][j] += max(cost[i-1][j], cost[i-1][j-1])

print(max(cost[n-1]))