from math import floor
n_tournaments = int(input())
initial_score = int(input())
final_score = initial_score
count_wins = 0

for _ in range(n_tournaments):
    step = input()
    if step == 'W':
        final_score += 2000
        count_wins += 1
    elif step == 'F':
        final_score += 1200
    else:
        final_score += 720

average_score = (final_score - initial_score) / n_tournaments
percent_wins = count_wins / n_tournaments * 100

print(f'Final points: {final_score}')
print(f'Average points: {floor(average_score)}')
print(f'{percent_wins:.2f}%')
