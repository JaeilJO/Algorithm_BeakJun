import sys
t = int(input())

for i in range(0,t):
    count,s= sys.stdin.readline().split()
    text = ''
    for j in s:
        text += j*int(count)
    print(text)    