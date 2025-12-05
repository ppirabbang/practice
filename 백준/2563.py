import sys

rows = 100
cols = 100
list_square = [[0] * cols for i in range(rows)]
count = int(sys.stdin.readline().rstrip())
square = 0

for i in range(count):
  width,height = map(int, sys.stdin.readline().split())
  for x in range(width,width+10):
    for y in range(height,height+10):
      if(list_square[x][y] == 1):
        square += 1
      else:
        list_square[x][y] = 1
  
print(count * 100 - square)


# import sys

# n = int(sys.stdin.readline())
# paper = set()  # 중복을 허용하지 않는 집합 생성

# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     # 색종이의 x, y 범위를 돌면서 좌표 자체를 집합에 넣음
#     for i in range(x, x + 10):
#         for j in range(y, y + 10):
#             paper.add((i, j)) # (x좌표, y좌표) 튜플을 넣음

# # set은 겹치는 좌표를 알아서 1개로 처리하므로 길이만 재면 끝
# print(len(paper))
