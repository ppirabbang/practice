import sys

N,K = map(int, sys.stdin.readline().split())
P = 1000000007

def factorial(n):
  result = 1
  for i in range(2,n+1):
    result = (result * i) % P
  return result

# 분자 N! 계산
numerator = factorial(N)

# 분모 K! * (N-K)! 계산
denominator = (factorial(K) * factorial(N-K)) % P

# 페르마의 소정리를 이용한 역원 계산
# denomiator 의 P-2 제곱을 P로 나눈 나머지
inverse = pow(denominator,P-2,P)

# 최종 결과 분자 * 분모 역원 % P
answer = (numerator * inverse) % P

print(answer)