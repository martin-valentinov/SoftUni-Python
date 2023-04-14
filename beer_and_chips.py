from math import ceil
name = input()
budget = float(input())
number_bottles = int(input())
number_packages = int(input())

price_bottles = number_bottles * 1.2
price_per_package = 0.45 * price_bottles
price_packages = price_per_package * number_packages
price_packages = ceil(price_packages)

total = price_packages + price_bottles
difference = abs(total - budget)

if budget >= total:
    print(f'{name} bought a snack and has {difference:.2f} leva left.')
else:
    print(f'{name} needs {difference:.2f} more leva!')
