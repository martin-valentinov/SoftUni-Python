world_record = float(input())
distance = float(input())
time_per_metre = float(input())

resistance = distance // 15
resistance *= 12.5

time = time_per_metre * distance + resistance

if time < world_record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')

else:
    difference = abs(world_record - time)
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
