budget = float(input())
n_video_cards = int(input())
n_processors = int(input())
n_memory = float(input())

video_cards = 250
video_cards_price = n_video_cards * video_cards
processor = video_cards_price * 0.35
processor_price = n_processors * processor
memory = video_cards_price * 0.1
memory_price = memory * n_memory

total_price = video_cards_price + processor_price + memory_price

if n_video_cards > n_processors:
    total_price *= 0.85

difference = abs(budget - total_price)

if total_price > budget:
    print(f'Not enough money! You need {difference:.2f} leva more!')

else:
    print(f'You have {difference:.2f} leva left!')
