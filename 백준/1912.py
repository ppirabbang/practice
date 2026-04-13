import sys

n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = N[0]

for i in range(1,n):
  dp[i] = max(N[i], dp[i-1] + N[i])

print(max(dp))