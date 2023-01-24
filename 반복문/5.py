import sys

test_cast = int(input())

for i in range(0,test_cast):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)