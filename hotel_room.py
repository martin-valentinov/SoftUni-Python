season = input()
stay_duration = int(input())

price_flat = 0
price_studio = 0

if season == 'May' or season == 'October':
    price_flat = 65 * stay_duration
    price_studio = 50 * stay_duration
    if 7 < stay_duration <= 14:
        price_studio *= 0.95
    elif 14 < stay_duration:
        price_studio *= 0.7
elif season == 'June' or season == 'September':
    price_studio = 75.2 * stay_duration
    price_flat = 68.7 * stay_duration
    if stay_duration > 14:
        studio *= 0.8
elif season == 'July' or season == 'August':
    studio = 76
    flat = 77

if stay_duration > 14:
    flat *= 0.9


print(f'Apartment: {price_flat:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')