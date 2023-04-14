temperature = int(input())
time = input()
outfit = ''
shoes = ''

if time == 'Morning':
    if 10 <= temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time == 'Afternoon':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

else:
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

