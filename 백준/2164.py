import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline())

for i in range(1,N+1):
  queue.append(i)

while(len(queue) != 1):
  queue.popleft()
  top = queue.popleft()
  queue.append(top)

print(queue[0])
