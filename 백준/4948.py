import sys

def is_prime(n):
  if(n < 2):
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if(n % i == 0):
      return False
  return True

N = int(sys.stdin.readline())
count = 0

while(N != 0):
  for k in range(N+1,2*N+1):
    if(is_prime(k)):
      count += 1
  print(count)

  count = 0
  N = int(sys.stdin.readline())