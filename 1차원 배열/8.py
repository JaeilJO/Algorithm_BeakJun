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