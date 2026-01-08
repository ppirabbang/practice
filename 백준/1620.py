import sys

name_to_id = {}
id_to_name = {}
N,M = map(int,sys.stdin.readline().split())

for i in range(1,N + 1):
  name = sys.stdin.readline().strip()
  name_to_id[name] = i
  id_to_name[i] = name

for _ in range(M):
  answer = sys.stdin.readline().strip()
  if(answer.isdigit()):
    print(id_to_name[int(answer)])
  elif(answer.isalpha()):
    print(name_to_id[answer])
    