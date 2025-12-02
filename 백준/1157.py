import sys

count = 0
list_int = [0] * 26
a = sys.stdin.readline().rstrip()

for i in a:
  list_int[ord(i.lower()) - 97] += 1

maximum = max(list_int)

for i in list_int: # i가 인덱스가 아님 list_int에 들어간 원소를 가리킴
  if(maximum == i):
    count += 1

if (count > 1):
  print("?")

elif (count == 1):
  max_index = list_int.index(maximum)
  #list.index(값) 함수는 리스트를 0번부터 훑으면서, 괄호 안의 '값'과 똑같은 값이 발견되면 그 즉시 그 자리가 몇 번째 칸(인덱스)인지 알려주고 끝납니다.
  print(chr(max_index + 65))
