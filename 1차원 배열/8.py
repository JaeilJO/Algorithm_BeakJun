import sys

test_case_count = int(input())

for _ in range(0, test_case_count):
    test_case = sys.stdin.readline()
    total_sum = 0
    o_count = 0
    for i in test_case:
        if i == "O":
            o_count += 1
            total_sum += o_count
        else:
            o_count = 0
    print(total_sum)

# 다른 정답
import sys

N = int(sys.stdin.readline())
for i in range(N):
    
    s = 0
    # X를 기준으로 list로 나눠줌
    a = sys.stdin.readline().rstrip().split('X')
    
    for v in a:
        # [00,00] 이런 식으로 나온 리스트의 아이템 하나의 길이를 재면 0의 갯수를 알 수 있음
        size = len(v)
        # 0 갯수에 0+1를더한 값을 곱하고 2로 나눈 몫이 위에서 말한 것의 공식이 됨
        s += (size * (size + 1)) // 2
        
    print(s)