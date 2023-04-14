number = int(input())
sum = 0
sum2 = 0

for _ in range (number):
    new_number = int(input())
    sum += new_number

for _ in range (number):
    new_number2 = int(input())
    sum2 += new_number2

if sum == sum2:
    print(f'Yes, sum = {sum}')

else:
    difference = abs(sum2 - sum)
    print(f'No, diff = {difference}')


