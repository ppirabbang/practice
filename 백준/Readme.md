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
- ex) 문자가 연속으로 나오거나 연속이 아니라면 문자열 안에서 한 번만 나와야 한다 --> unique 와 같이 어려운 생각 하지 말고 일단
- 문자가 연속으로 나온다 -> 다음 인덱스 문자가 같은 경우는 상관 없고 다르다면 -> 문자열 안에서 한 번만 나와야 한다 -> 해당 인덱스 이후부터 끝까지 찾기 -> word[j] in word[j+1:]  
- 소수점 몇 째 자리까지 --> print("%.6f", 계산식~!) 과 같이 표현, 25206 최적화 코드 참고
- [[0] * cols for i in range(rows)] 2차원 배열 선언 방법
- 중복된 걸 1개로 처리해주는 set() 함수를 사용해서 겹치는 부분의 넓이 등에 활용하면 좋을 듯, paper = set() paper.add(x좌표,y좌표) 하면 알아서 겹치는건 1개로 처리해준다 이후 길이를 반환하면 넓이와 동일하다
- numbers = [1, 2, 3]
1. map(str, numbers) -> 숫자들을 전부 문자로 변환 ('1', '2', '3')
2. 그 다음 join으로 연결
  result = " + ".join(map(str, numbers))
  print(result)
  결과: 1 + 2 + 3
