- map(int, input().split())
- list_int = list(map(int,sys.stdin.readline().split()) 이 입력한 숫자들 배열에 넣는 방법
- b = "abc" 에서 b[0] b[1] b[2] 와 같이 인덱싱 가능, 끝 자리는 b[-1] 도 되는데 개행문자가 들어가니까 rstrip() 써주면 됨
- import sys
  N = int(sys.stdin.readline().rstrip()) 이 입력이 더 빠름, rstrip() 은 자동으로 붙는 개행문자 제거
- map(int, sys.stdin.readline().split()) 가능
- print("long", end="") 식으로 하면 반복문도 한 줄로 출력 가능, 반복문 밖에서 print 해도 한 줄로 출력됨
- 최대 최소 문제 maximum = max(list_int) minimum = min(list_int) 와 같이 함수 쓸 생각해야 됨
- 파이썬은 temp 두고 바꿀 필요 없이  a,b = b,a 가능함,, a[0] = a[2] 와 같이 바꾸는건 안됨(immuatable), 그래서 문자열을 뒤집으려면 a = a[::-1] 로 해야됨
- print(len(sys.stdin.readline())) 을 하면 당연히 문자열 마지막 \0 도 포함 되므로 -1 을 해줘야 함
- ord() : (A -> 65) 
  chr() : (65 -> A)
- find() 는 처음 나오는 위치를 반환함, 이후에 나오는 걸 찾으려면 first = text.find('a') second = text.find('a', first + 1) 로 해야됨
- groups = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"] ,,, for i,g in enumerate(groups): 하면 i 에는 인덱스 g에는 배열 원소가 들어감
- for i in list_int: # i가 인덱스가 아님 list_int에 들어간 원소를 가리킴
- max_index = list_int.index(maximum)
  #list.index(값) 함수는 리스트를 0번부터 훑으면서, 괄호 안의 '값'과 똑같은 값이 발견되면 그 즉시 그 자리가 몇 번째 칸(인덱스)인지 알려주고 끝납니다.
- 중복되는 문자열을 찾을 때(2941번) 간단한 특수 문자나 알아볼 수 있는 문자로 변환하는 아이디어 
