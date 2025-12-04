import sys

all_score = 0
all_grade = 0

for i in range(20):
  title, score, grade = map(str, sys.stdin.readline().split())
  if(grade == "P"):
    continue
  else:
    if(grade == "A+"):
      all_score += 4.5 * float(score)
      all_grade += float(score)
    elif(grade == "A0"):
      all_score += 4.0 * float(score)
      all_grade += float(score)
    elif(grade == "B+"):
      all_score += 3.5 * float(score)
      all_grade += float(score)
    elif(grade == "B0"):
      all_score += 3.0 * float(score)
      all_grade += float(score)
    elif(grade == "C+"):
      all_score += 2.5 * float(score)
      all_grade += float(score)
    elif(grade == "C0"):
      all_score += 2.0 * float(score)
      all_grade += float(score)
    elif(grade == "D+"):
      all_score += 1.5 * float(score)
      all_grade += float(score)
    elif(grade == "D0"):
      all_score += 1.0 * float(score)
      all_grade += float(score)
    else:
      all_grade += float(score)

print(float(all_score / all_grade))
    