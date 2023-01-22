hour,minute = map(int,input().split())

# 시간을 분으로 바꾼뒤 45를 빼주기
total = hour * 60 + minute - 45

# 이때 45를 뺏을경우 0보다 작으면 
# 0보다 작은경우면 hour가 0인 경우이다.
# 즉 24시인 경우 이니까 60분에 24시간을 곱해준다.
if total < 0:
    total += 60 * 24

# 시간은 total의 몫이다
hour = total // 60

# 분은 total의 나머지이다.
minute = total % 60

print(hour,minute)