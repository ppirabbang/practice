import sys

count = int(sys.stdin.readline().rstrip())
group_count = count


for i in range(count):
  word = sys.stdin.readline().rstrip()
  for j in range(len(word) -1):
      if(word[j] != word[j+1]):
        if(word[j] in word[j+1:]):
          group_count -= 1
          break

print(group_count)