n_of_chicken_menus = int(input())
n_of_fish_menus = int(input())
n_of_vegetarian_menus = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15

price = n_of_chicken_menus * chicken_menu_price + n_of_fish_menus * fish_menu_price + \
    n_of_vegetarian_menus * vegetarian_menu_price

desert = price * 0.2

price = price + desert + 2.50

print(price)


