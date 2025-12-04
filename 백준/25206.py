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

###
import sys

# 등급별 점수를 딕셔너리로 정의 (F는 0점 처리)
rating_table = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total_point = 0  # 학점 * 과목평점의 합 (분자)
total_credit = 0 # 총 학점의 합 (분모)

for _ in range(20):
    line = sys.stdin.readline().split()
    # line[0]: 과목명, line[1]: 학점, line[2]: 등급
    
    score = float(line[1]) # 학점
    grade = line[2]        # 등급

    if grade == "P":
        continue
    
    # 딕셔너리를 사용하여 점수 계산 간소화
    total_point += score * rating_table[grade]
    total_credit += score

# 0으로 나누는 에러 방지 (혹시 모를 예외 처리)
if total_credit == 0:
    print(0.0)
else:
    print(total_point / total_credit)
###
    
