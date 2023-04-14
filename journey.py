budget = float(input())
season = input()
expense = 0
destination = ''
type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expense += 0.3 * budget
    elif season == 'winter':
        expense += 0.7 * budget
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expense += 0.4 * budget
    elif season == 'winter':
        expense += 0.8 * budget
else:
    destination = 'Europe'
    expense += 0.9 * budget

if season == 'winter' or destination == 'Europe':
    type = 'Hotel'
else:
    type = 'Camp'

print(f'Somewhere in {destination}')
print(f'{type} - {expense:.2f}')