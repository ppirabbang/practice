import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
  command = list(map(str, sys.stdin.readline().split()))

  if(command[0] == "push"):
    queue.append(int(command[1]))
  elif(command[0] == "pop"):
    if(not queue):
      print(-1)
    else:
      front = queue.popleft()
      print(front)
  elif(command[0] == "size"):
    print(len(queue))
  elif(command[0] == "empty"):
    if(not queue):
      print(1)
    else:
      print(0)
  elif(command[0] == "front"):
    if(not queue):
      print(-1)
    else:
      print(queue[0])
  elif(command[0] == "back"):
    if(not queue):
      print(-1)
    else:
      print(queue[-1])