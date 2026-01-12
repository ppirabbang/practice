import sys

T = int(sys.stdin.readline())


for i in range(T):
  max = 0
  list_A = []
  set_B = set()
  A,B = map(int,sys.stdin.readline().split())
  for i in range(1,A+1):
    if(A % i == 0):
      list_A.append(i)

  for k in range(1,B+1):
    if(B % k == 0):
      set_B.add(k)

  for j in list_A:
    if(j in set_B):
      max = j

  print(max * (A // max) * (B // max))
  