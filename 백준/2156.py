import sys

n = int(sys.stdin.readline())
list_int = []
dp = [0] * (n+1)

for i in range(n):
  N = int(sys.stdin.readline())
  list_int.append(N)

if n == 1:
    print(list_int[0])
    exit()
elif n == 2:
    print(list_int[0] + list_int[1])
    exit()

dp[0] = list_int[0]
dp[1] = list_int[0] + list_int[1]
dp[2] = max(dp[1], list_int[0] + list_int[2], list_int[1] + list_int[2])
for i in range(3,n):
  dp[i] = max(dp[i-1], dp[i-2] + list_int[i], dp[i-3] + list_int[i-1] + list_int[i])

print(dp[n-1])