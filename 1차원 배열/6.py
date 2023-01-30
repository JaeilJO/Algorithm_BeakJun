import sys

remainders = []
for i in range(0,10):
    remainder = int(sys.stdin.readline())%42
    remainders.append(remainder)

print(len(set(remainders)))