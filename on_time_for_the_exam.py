hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

time_exam = hour_exam * 60 + minute_exam
time_arrival = hour_arrival * 60 + minute_arrival

if time_exam - 30 <= time_arrival <= time_exam:
    print('On time')
elif time_arrival < time_exam - 30:
    print('Early')
else:
    print('Late')

difference = abs(time_exam - time_arrival)
hour = difference // 60
minute = difference % 60

if time_exam - 60 < time_arrival < time_exam:
    print(f'{difference} minutes before the start')
elif time_exam - 60 >= time_arrival:
    print(f'{hour}:{minute:02d} hours before the start')
elif time_arrival >= time_exam + 60:
    print(f'{hour}:{minute:02d} hours after the start')
elif time_arrival > time_exam:
    print(f'{difference} minutes after the start')