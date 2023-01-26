N = int(input())

# 첫자리 수
first = N//10

# 둘째자리 수
second = N%10

i=0

while True:
    # 둘째자리수의 첫번째 수와 처음주어진 첫째자리 수와 둘째자리수의 합의 둘째자리 수의 합
    c = second*10 + (first+second)%10
    first = c//10
    second = c%10
    i+=1

    if c==N:
        break
    else:
        continue

print(i)
    