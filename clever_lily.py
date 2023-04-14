age = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())
total_money = 0
gift_money = 0
number_toys = 0

for n in range(1, age + 1):
    if n % 2 == 0:
        gift_money += 10
        total_money += gift_money - 1
    else:
        number_toys += 1
total_money += number_toys * price_per_toy
difference = abs(total_money - price_washing_machine)

if total_money >= price_washing_machine:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')



