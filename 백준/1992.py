import sys

N = int(sys.stdin.readline())
list_N = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def cut(row, column, n):
  num = list_N[row][column]
  for i in range(row, row+n):
    for j in range(column, column+n):
      if(list_N[i][j] != num):
        print("(", end="")
        cut(row, column, n//2)
        cut(row, column + n//2 , n//2)
        cut(row + n//2 , column, n//2)
        cut(row + n//2, column + n//2, n//2)
        print(")", end="")
        return
      
  print(num,end="")

cut(0,0,N)