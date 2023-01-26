import sys

numbers = []

for i in range(0,9):
  numbers.append(int(sys.stdin.readline()))

max_number = max(numbers)
max_number_index = numbers.index(max_number)+1

print("{}\n{}".format(max_number,max_number_index))