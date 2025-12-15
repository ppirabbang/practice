import sys

N = int(sys.stdin.readline())

while(N > 1):
  for i in range(2,N+1):
    while(N % i == 0):
      print(i)
      N = N // i

#import sys

#N = int(sys.stdin.readline())

# 2부터 하나씩 나누기 시작
#i = 2

# i * i <= N 일 때까지만 반복 (즉, i가 제곱근 N보다 작을 때까지만)
#while i * i <= N:
#    while N % i == 0:
#        print(i)
#        N //= i
#    i += 1

# 반복문 종료 후에도 N이 1보다 크다면, 
# 남은 N은 그 자체로 소수라는 뜻입니다.
#if N > 1:
#    print(N)

# 제곱근까지만 확인하는 이유 : N = A * B 라고 할 때 A.B 가 sqrt(N) 보다 크다고 가정한다면 A * B > N 이게 되므로 가정이 틀림