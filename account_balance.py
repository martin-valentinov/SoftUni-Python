total = 0

while True:
    number = input()
    if number == 'NoMoreMoney':
        break
    elif float(number) <= 0:
        print('Invalid operation!')
        break
    elif float(number) > 0:
        total += float(number)
        print(f'Increase: {float(number):.2f}')

print(f'Total: {total:.2f}')