
#점수 / M * 100

N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

scores_sum = 0

for i in scores:
    new_score = i / M * 100
    scores_sum += new_score
    
print(scores_sum/N)
