import sys


x = []
y = []

for i in range(int(sys.stdin.readline())):
  x_, y_ = map(int,sys.stdin.readline().split())
  x.append(x_)
  y.append(y_)

if(len(x) == 1):
  print(0)
else:
  min_x = min(x)
  min_y = min(y)
  max_x = max(x)
  max_y = max(y)
  print((max_x - min_x) * (max_y - min_y)) 
