holiday_price = float(input())
n_puzzle = int(input())
n_dolls = int(input())
n_teddybears = int(input())
n_minions = int(input())
n_trucks = int(input())

puzzle = 2.6
dolls = 3
teddybear = 4.1
minion = 8.2
truck = 2

total = n_puzzle * puzzle + n_dolls * dolls + n_teddybears * teddybear + n_minions * minion + n_trucks * truck
number_of_products = n_dolls + n_trucks + n_minions + n_puzzle + n_teddybears

if number_of_products >= 50:
    total -= total * 0.25

total -= total * 0.1

if total >= holiday_price:
    money_left = abs(holiday_price - total)
    print(f'Yes! {money_left:.2f} lv left.')

else:
    money_needed = abs(holiday_price - total)
    print(f'Not enough money! {money_needed:.2f} lv needed.')

