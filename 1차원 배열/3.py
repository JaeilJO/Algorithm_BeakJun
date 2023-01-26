
N = int(input())
numbers = list(map(int,input().split()))

print(min(numbers),max(numbers))


# 괜찮은 답
import sys
# 이건 필요없으니까 건너띄기 용으로 추가해준 느낌
input()

# for문을 한줄로 표현 하는 방법
# read는 byte를 지정해주지 않으면 끝나지 않는데 아마 beakjoon을 풀때 이러한 방법을 사용하는 것 같다
a = [int(s) for s in sys.stdin.read().split()]
print(min(a))