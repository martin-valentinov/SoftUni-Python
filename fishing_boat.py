budget = int(input())
season = input()
n_fishers = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
else:
    price = 2600

if n_fishers <= 6:
    price *= 0.9
elif 7 <= n_fishers <= 11:
    price *= 0.85
else:
    price *= 0.75

if n_fishers % 2 == 0 and season != 'Autumn':
    price *= 0.95

difference = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')