import sys


x_ = []
y_ = []

for i in range(3):
  a,b = map(int,sys.stdin.readline().split())
  x_.append(a)
  y_.append(b)
  

for i in range(3):
  if(x_.count(x_[i]) == 1):
    x = x_[i]
  if(y_.count(y_[i]) == 1):
    y = y_[i]

print(x,y)

# for _ in range(3):
#     x, y = map(int, input().split())
#     x4 ^= x  # x 좌표들을 모두 XOR 연산
#     y4 ^= y  # y 좌표들을 모두 XOR 연산

# print(x4, y4)