name = input()
times_failed = 0
grade = 1
total = 0

while times_failed < 2:
    mark = float(input())
    if mark < 4:
        times_failed += 1
    else:
        grade += 1
        total += mark
    if grade > 12:
        break

if grade > 12:
    average = total / 12
    print(f'{name} graduated. Average grade: {average:.2f}')
else:
    print(f'{name} has been excluded at {grade} grade')