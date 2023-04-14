budget = float(input())
extras = int(input())
price_per_dress = float(input())
decoration = budget * 0.1
total_dress_price = extras * price_per_dress

if extras > 150:
    total_dress_price *= 0.9

expenses = decoration + total_dress_price
difference = abs(budget - expenses)

if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')

else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')