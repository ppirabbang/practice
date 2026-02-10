import sys

count_fib = 0
count_fibo = 0
def fib(n):
  global count_fib
  if(n == 1 or n == 2):
    count_fib += 1
    return 1
  else:
    return (fib(n-1) + fib(n - 2))
  
def fibonacci(n):
  global count_fibo
  for i in range(2,n):
    count_fibo += 1
    f[i] = f[0] + f[1]
  return f[n-1]

n = int(sys.stdin.readline())
f = [0] * 41
f[0] = f[1] = 1
fib(n)
fibonacci(n)

print(count_fib, end=" ")
print(count_fibo)