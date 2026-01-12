import sys

def get_gcd(a,b):
  while(b > 0):
    a,b = b, a % b
  return a

A1,B1 = map(int, sys.stdin.readline().split())
A2,B2 = map(int, sys.stdin.readline().split())

up = A1 * B2 + A2 * B1
down = B1 * B2

gcd = get_gcd(up, down)
print(up // gcd , down // gcd)