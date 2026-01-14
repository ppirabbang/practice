import sys

def is_prime(N):
  if(N < 2):
    return False
  for i in range(2,int(N ** 0.5) + 1):
    if(N % i == 0):
      return False
  return True

a,b = map(int, sys.stdin.readline().split())

for i in range(a,b+1):
  if(is_prime(i)):
    print(i)