import sys

a = int(sys.stdin.readline())
count = 0
numbers = list(map(int,sys.stdin.readline().split()))


for i in numbers:
  if (i <= 1):
    continue
  
  is_prime = True
  for k in range(2,i):
    if(i % k == 0):
      is_prime = False
      break

  if(is_prime):
    count += 1
print(count) 
