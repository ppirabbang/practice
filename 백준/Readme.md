- map(int, input().split())
- list_int = list(map(int,sys.stdin.readline().split()) 이 입력한 숫자들 배열에 넣는 방법
- b = "abc" 에서 b[0] b[1] b[2] 가능
- import sys
  N = int(sys.stdin.readline().rstrip()) 이 입력이 더 빠름, rstrip() 은 자동으로 붙는 개행문자 제거
- map(int, sys.stdin.readline().split()) 가능
- print("long", end="") 식으로 하면 반복문도 한 줄로 출력 가능, 반복문 밖에서 print 해도 한 줄로 출력됨
- 최대 최소 문제 maximum = max(list_int) minimum = min(list_int) 와 같이 함수 쓸 생각해야 됨
- 파이썬은 temp 두고 바꿀 필요 없이  a,b = b,a 가능함
