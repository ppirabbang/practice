import sys

while(1):
  a = int(sys.stdin.readline())
  if(a == -1):
    break

  list_int = []
  sum = 0

  for i in range(1,a):
    if(a % i == 0):
      sum += i
      list_int.append(i)

  if(a == sum):
    print(f"{sum} = ", end="")
    for i in range(len(list_int)):
      print(list_int[i], end="")
      if(i != len(list_int) -1):
        print(" + ", end="")
    print()
    
  else:
    print(f"{a} is NOT perfect.")
      