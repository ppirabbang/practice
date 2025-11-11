sum = int(input())
count = int(input())

total = 0
for i in range(count):
  price, small_count = map(int,(input()))
  total += (price * small_count)

if total == sum :
  print("Yes")
else:
  print("No")