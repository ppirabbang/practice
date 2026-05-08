import sys

N = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt_1, cnt_0, cnt__1 = 0,0,0
def cut(row,column,n):
  global cnt_1, cnt_0, cnt__1
  num = tri[row][column]
  for i in range(row, row + n):
    for j in range(column, column + n):
      if(num != tri[i][j]):
        cut(row, column, n//3)
        cut(row, column + n//3 , n//3)
        cut(row, column + n // 3 * 2, n//3)
        cut(row + n//3 , column, n//3)
        cut(row + n//3, column + n//3, n//3)
        cut(row + n//3, column + n//3 * 2, n//3)
        cut(row + n//3 * 2, column, n//3)
        cut(row + n//3 * 2, column + n//3, n//3)
        cut(row + n//3 * 2, column + n//3 * 2, n//3)
        return
    
  if num == -1:
    cnt__1 += 1
  elif num == 0:
    cnt_0 += 1
  else:
    cnt_1 += 1

cut(0,0,N)
print(cnt__1)
print(cnt_0)
print(cnt_1)

        
