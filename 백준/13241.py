import sys

def get_gcd(a,b):
  while(b > 0):
    a,b = b, a % b
  return a

A,B = map(int,sys.stdin.readline().split())
  
gcd = get_gcd(A,B)
lcm = (A * B) // gcd

print(lcm)
