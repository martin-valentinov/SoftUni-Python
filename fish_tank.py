length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

volume = length_cm * width_cm * height_cm
volume_litres = volume / 1000
percent /= 100
volume_litres = volume_litres - (volume_litres * percent)

print(volume_litres)