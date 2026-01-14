# import sys

# def is_prime(n):
#   if(n < 2):
#     return False
#   for i in range(2, int(n ** 0.5) + 1):
#     if(n % i == 0):
#       return False
#   return True

# T = int(sys.stdin.readline())

# for i in range(T):
#   list_int = []
#   set_int = set()
#   count = 0

#   N = int(sys.stdin.readline())
#   for k in range(3, N+1):
#     if(is_prime(k)):
#       list_int.append(k)
#       set_int.add(k)

#   for j in list_int:
#     if((N - j) in set_int):
#       count += 1
  
#   print(count // 2)
# 이러면 중간을 제곱수는 중간을 포함 안하면 갯수가 덜 나오고 제곱수가 아니면 3+5 5+3 중복됨

import sys

MAX_ = 1000000
is_prime = [True] * (MAX_ + 1)
is_prime[0] = is_prime[1] = False

for i in range(2,int(MAX_ ** 0.5) + 1):
  if(is_prime[i]):
    for j in range(i*i, MAX_ + 1, i):
      is_prime[j] = False

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  count = 0

  for i in range(2, N//2+1):
    if(is_prime[i] and is_prime[N-i]):
      count += 1
    
  print(count)
