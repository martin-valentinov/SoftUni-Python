number_locations = int(input())


for x in range(number_locations):
    expected_gold = float(input())
    days_mining = int(input())
    total = 0
    for d in range(days_mining):
        gold_per_day = float(input())
        total += gold_per_day
    average = total / days_mining
    if average >= expected_gold:
        print(f'Good job! Average gold per day: {average:.2f}.')
    else:
        difference = abs(expected_gold - average)
        print(f'You need {difference:.2f} gold.')