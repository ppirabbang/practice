import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
prime_list = []

for i in range(N,M+1):
  if(i == 1):
    continue

  is_prime = True

  for j in range(2,i):
    if(i % j == 0):
      is_prime = False
      break

  if(is_prime):
    prime_list.append(i)

if(len(prime_list) > 0):
  print(sum(prime_list))
  print(min(prime_list))

else:
  print(-1)
    