import sys

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))

max_value = -1000000000
min_value = 1000000000

def dfs(depth, sum, plus, minus, mul, div):
  global max_value, min_value
  if(depth == N):
    max_value = max(max_value,sum)
    min_value = min(min_value,sum)
    return
  
  if(plus > 0):
    dfs(depth+1, sum + number[depth], plus -1, minus, mul, div)
  if(minus > 0):
    dfs(depth+1, sum - number[depth], plus, minus -1, mul, div)
  if(mul > 0):
    dfs(depth+1, sum * number[depth], plus, minus, mul-1, div)
  if(div > 0):
    dfs(depth+1, int(sum / number[depth]), plus, minus, mul, div-1)



dfs(1,number[0],ops[0],ops[1],ops[2],ops[3])
print(max_value)
print(min_value)