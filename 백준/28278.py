import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):  
  list_int = list(map(int,sys.stdin.readline().split()))
  
  if(list_int[0] == 1):
    stack.append(list_int[1])
    list_int.clear()
  
  elif(list_int[0] == 2):
    if not stack:
      print(-1)
    else:
      top = stack.pop()
      print(top)
  
  elif(list_int[0] == 3):
    print(len(stack))
  
  elif(list_int[0] == 4):
    if not stack:
      print(1)
    else:
      print(0)

  elif(list_int[0] == 5):
    if not stack:
      print(-1)
    else:
      print(stack[-1]) # stack의 top
  
