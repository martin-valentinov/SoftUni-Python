import sys
n = int(input())
max_number = -sys.maxsize
total = 0

for _ in range (n):
    number = int(input())
    if number > max_number:
        max_number = number
    total += number
total_rest = total - max_number
if total_rest == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference = abs(total_rest - max_number)
    print('No')
    print(f'Diff = {difference}')

