days = int(input())
room = input()
feedback = input()
total = 0

nights = days - 1

if room == 'room for one person':
    total = 18 * nights
elif room == 'apartment':
    total = 25 * nights
    if days < 10:
        total *= 0.7
    elif 10 <= days <= 15:
        total *= 0.65
    else:
        total *= 0.5
else:
    total = 35 * nights
    if days < 10:
        total *= 0.9
    elif 10 <= days <= 15:
        total *= 0.85
    else:
        total *= 0.8

if feedback == 'positive':
    total *= 1.25
else:
    total *= 0.9

print(f'{total:.2f}')

