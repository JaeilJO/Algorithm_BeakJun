import sys
numbers = [i for i in range(1,31)]

for _ in range(28):
    numbers.remove(int(sys.stdin.readline()))

print(numbers[0])
print(numbers[1])

