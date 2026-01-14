import sys

def is_prime(x):
  if(x < 2):
    return False
  for i in range(2, int(x ** 0.5) + 1):
    if(x % i == 0):
      return False
  return True

T = int(sys.stdin.readline())
for i in range(T):
  N = int(sys.stdin.readline())
  while True:
    if(is_prime(N)):
      print(N)
      break
    N += 1