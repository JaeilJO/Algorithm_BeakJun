X = int(input())
N = int(input())

total_cost = 0

for i in range(0,N):
    a, b = map(int,input().split())
    cost = a * b
    total_cost += cost

if total_cost == X :
    print('Yes')
else:
    print('No')