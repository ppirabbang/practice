import sys

N = int(sys.stdin.readline())
list_line = list(map(int, sys.stdin.readline().split()))
stack_wait = []
k = 1

while(list_line):
  list_top = list_line.pop(0)
  if(list_top == k):
    k += 1
  else:
    stack_wait.append(list_top)

  while(stack_wait and stack_wait[-1] == k):
    stack_wait.pop()
    k += 1

if(not stack_wait):
  print("Nice")
else:
  print("Sad")