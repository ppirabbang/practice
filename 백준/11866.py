import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
queue = deque(range(1, N+1))
list_answer = []

while(queue):
  for _ in range(K-1):
    queue.append(queue.popleft())
  list_answer.append(queue.popleft())

print(f"<{', '.join(map(str, list_answer))}>")