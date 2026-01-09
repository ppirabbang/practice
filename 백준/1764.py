import sys

N,M = map(int, sys.stdin.readline().split())
count = 0

set_N = set(sys.stdin.readline().strip() for _ in range(N))
list_M = set(sys.stdin.readline().strip() for _ in range(M))
list_answer = []

for name in list_M:
  if(name in set_N):
    list_answer.append(name)
    count += 1

list_answer.sort()
print(count)
for i in list_answer:
  print(i)