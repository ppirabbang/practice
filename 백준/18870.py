import sys

N = int(sys.stdin.readline())
list_int = list(map(int,sys.stdin.readline().split()))

set_int = sorted(list(set(list_int)))
dict_int = {value:index for index, value in enumerate(set_int)}

for i in list_int:
  print(dict_int[i], end=" ")