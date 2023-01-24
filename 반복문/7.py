import sys


test_cast = int(input())

for i in range(1,test_cast+1):
    a, b = map(int,sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i,a,b,a+b))

