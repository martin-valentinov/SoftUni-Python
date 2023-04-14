hour = int(input())
minute = int(input())

minute += 15

hour *= 60
time = hour + minute

hour = time // 60
minute = time % 60

if hour == 24:
    hour = 0

if minute < 9:
    print(f'{hour}:0{minute}')

else:
    print(f'{hour}:{minute}')
