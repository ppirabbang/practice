import sys

N = int(sys.stdin.readline())
set_name = set()

for i in range(N):
  name, where = map(str, sys.stdin.readline().split())
  if(where == "enter"):
    set_name.add(name)
  elif(where == "leave"):
    set_name.remove(name)

sort_list = sorted(list(set_name), reverse=True)
for i in sort_list:
  print(i)