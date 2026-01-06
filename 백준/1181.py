import sys

N = int(sys.stdin.readline())

list_set = set(sys.stdin.readline().strip() for _ in range(N))
list_string = list(list_set)
list_string.sort(key = lambda x : (len(x),x))


for i in list_string:
  print(i)