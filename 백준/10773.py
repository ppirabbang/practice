import sys

K = int(sys.stdin.readline())
stack = []
sum = 0

for _ in range(K):
  N = int(sys.stdin.readline())
  if(N == 0):
    if not stack: # 비었다면
      stack.append(0)
    else:
      stack.pop()
  else:
    stack.append(N)

for i in stack:
  sum += i
print(sum)