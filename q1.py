price_per_page = float(input())
price_per_cover = float(input())
discount_percent = int(input())
designer_costs = float(input())
paid_percent = int(input())

price = price_per_page * 899 + price_per_cover * 2
price -= price * discount_percent / 100
price += designer_costs
price -= price * paid_percent / 100

print(f'Avtonom should pay {price:.2f} BGN.')
