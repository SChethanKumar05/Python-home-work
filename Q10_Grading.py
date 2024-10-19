total_score = 0
subj =5

for i in range(1 , subj+1):
    score = int(input(f"input the subj score {i} in range 1-100"))

    while score<1 or score>100:
        print("invalid score")
        score = int(input(f"enter the valid score fpr subjet {i} bw 1-100"))
    total_score += score

avg_score = total_score/subj

if avg_score >= 90:
    grade = 'A'
elif avg_score >= 80:
    grade = 'B'
elif avg_score >= 70:
    grade = 'C'
elif avg_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"the average score {avg_score}")
print(f"\ngrade = {grade}")