actors_name = input()
academy_points = float(input())
n_jurors = int(input())


for x in range(n_jurors):
    name_juror = input()
    point = float(input())
    academy_points += (len(name_juror) * point / 2)
    if academy_points > 1250.5:
        break
if academy_points > 1250.5:
    print(f'Congratulations, {actors_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    difference = abs(1250.5 - academy_points)
    print(f'Sorry, {actors_name} you need {difference:.1f} more!')

