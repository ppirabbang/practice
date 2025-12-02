import sys

alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().rstrip()

for i in alphabet:
  word = word.replace(i,"*")

print(len(word))
