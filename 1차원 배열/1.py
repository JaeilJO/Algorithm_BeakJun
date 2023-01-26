# 내방법
N = int(input())
numbers = input().split()
v = input()

count = 0

for i in range(0,N):
    if numbers[i] == v:
        count += 1

print(count)


# 좋은 방법
N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

print(numbers.count(v))