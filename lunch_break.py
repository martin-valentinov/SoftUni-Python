from math import ceil
series_name = str(input())
series_length = int(input())
break_length = int(input())

lunch_length = break_length / 8
relaxation_time = break_length / 4

time_left = break_length - lunch_length - relaxation_time
free_time = abs(time_left - series_length)

if time_left >= series_length:
    print(f'You have enough time to watch {series_name} and left with {ceil(free_time)} minutes free time.')

else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(free_time)} more minutes.")