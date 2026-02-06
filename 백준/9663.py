import sys

def sol(n):
  global N,count

  if(n == N):
    count += 1
    return
  
  for i in range(N):
    if(not used_column[i] and not used_up[i+n] and not used_down[n-i + (N-1)]):
      used_column[i] = True
      used_up[i+n] = True
      used_down[n-i + (N-1)] = True
      sol(n+1)
      used_column[i] = False
      used_up[i+n] = False
      used_down[n-i + (N-1)] = False

N = int(sys.stdin.readline())
count = 0
used_column = [False] * N
used_up = [False] * (2*(N-1)+1)
used_down = [False] * (2*(N-1)+1)

sol(0)
print(count)