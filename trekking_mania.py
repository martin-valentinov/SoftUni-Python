number_groups = int(input())
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0

for n in range(number_groups):
    people_per_group = int(input())
    if people_per_group <= 5:
        m1 += people_per_group
    elif people_per_group <= 12:
        m2 += people_per_group
    elif people_per_group <= 25:
        m3 += people_per_group
    elif people_per_group <= 40:
        m4 += people_per_group
    else:
        m5 += people_per_group

total = m1 + m2 + m3 + m4 + m5
percent1 = m1 / total * 100
percent2 = m2 / total * 100
percent3 = m3 / total * 100
percent4 = m4 / total * 100
percent5 = m5 / total * 100
print(f'{percent1:.2f}%')
print(f'{percent2:.2f}%')
print(f'{percent3:.2f}%')
print(f'{percent4:.2f}%')
print(f'{percent5:.2f}%')


