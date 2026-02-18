import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = m[0]

for i in range(1,n):
  #dp의 각 원소가 1개,2개 값을 더하는게 맞지만 max를 통해 시작 위치를 정하는 것. 만약 6개의 합이 -2 이고 7번째가 3인 경우 앞에 결과를 버리고 7번째 수만 가져가는게 최댓값임. 그러면 7번째가 시작인 연속된 원소 합이 최댓값이 되는거임.
  dp[i] = max(m[i], dp[i-1] + m[i])

print(max(dp))