A,B = input().split()

A = A[2] + A[1] + A[0]
B = B[2] + B[1] + B[0]
print(max(int(A),int(B)))

# list[A:B:C]
# A부터 B까지 C의 간격으로 뽑아내라는 의미
# C에 음수가 들어가면 거꾸로 진행한다

# 좋은 방법
print(max(input()[::-1].split()))

