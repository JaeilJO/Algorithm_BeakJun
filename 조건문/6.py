hour, minute = map(int,input().split())

cooking_time = int(input())


#cooking time은 분으로 주어진다 그러므로 minute와 더해준다
# 그리고 60으로 나눠주는 몫은 시간이 된다. 그러므로 hour와 더해준다
# 그 값을 24에 나누면 몫은 시간이 된다.
finish_hour = (hour+(minute+cooking_time)//60)%24

# 나머지는 분이 된다
finish_minute = (minute+cooking_time) % 60

print(finish_hour,finish_minute)