import sys

list_int = [False] * 30

for i in range(28):
  student = int(sys.stdin.readline())
  list_int[student-1] = True

for i in range(30):
  if list_int[i] == False:
    print(i+1)