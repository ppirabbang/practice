import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
list_temp = list(map(int,sys.stdin.readline().split()))
for i in range(N):
  queue.append([list_temp[i],i+1] )
result = []


while(queue):
  val,idx = queue.popleft()
  result.append(idx)

  if not queue:
    break

  if(val > 0):
    for _ in range(val - 1): # 여기서는 popleft 된 상태의 queue를 상대로 하니까 이미 오른쪽으로 한 칸 간거나 다름없음
      queue.append(queue.popleft())
    
  
  elif(val < 0):
    for _ in range((val * -1)):
      queue.appendleft(queue.pop())
    
for i in result:
  print(i, end=" ")
  