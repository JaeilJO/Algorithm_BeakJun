def solve(a):
    sum = 0
    for i in range(0,len(a)):
        sum += a[i]
    return sum


# 좀 더 올바른 방법
def solve(a):
    return sum(a)