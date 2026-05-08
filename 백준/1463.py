import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)

for i in range(2,n+1):
  dp[i] = dp[i-1] + 1

  if(i%2 == 0):
    dp[i] = min(dp[i], dp[i//2] + 1)

  if(i%3 == 0):
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

# 어떤 숫자에 집중하기 보다 그 숫자를 구하기 위한 횟수에 집중을 해야 그게 dp 이기도 하고