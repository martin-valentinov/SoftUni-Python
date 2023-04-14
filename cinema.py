type = input()
rows = int(input())
columns = int(input())
price = 0

if type == 'Premiere':
    price = 12
elif type == 'Normal':
    price = 7.5
else:
    price = 5

total = rows * columns * price
print(f'{total:.2f} leva')