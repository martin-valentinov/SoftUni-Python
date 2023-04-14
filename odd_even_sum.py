number = int(input())
sum1 = 0
sum2 = 0

for x in range (number):
    num = int(input())
    if x % 2 == 0:
        sum1 += num
    else:
        sum2 += num

difference = abs(sum1 - sum2)

if sum1 == sum2:
    print('Yes')
    print(f'Sum = {sum1}')
else:
    print('No')
    print(f'Diff = {difference}')