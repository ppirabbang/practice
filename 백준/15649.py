import sys


def solve():
  N, M = map(int, sys.stdin.readline().split())

  visited = [False] * (N+1)
  s = []

  def dfs():
    if len(s) == M:
      print(' '.join(map(str,s)))
      return
    
    for i in range(1, N+1):
      if not visited[i]:
        visited[i] = True
        s.append(i)

        dfs()

        s.pop()
        visited[i] = False
  
  dfs()

if __name__ == "__main__":
  solve()