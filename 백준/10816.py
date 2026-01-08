import sys

card_dict = {}

N = int(sys.stdin.readline())
list_card = list(map(int, sys.stdin.readline().split()))

for i in list_card:
  if(i in card_dict):
    card_dict[i] += 1
  else:
    card_dict[i] = 1

M = int(sys.stdin.readline())
find_card = list(map(int, sys.stdin.readline().split()))

for i in find_card:
  print(card_dict.get(i,0), end=" ")