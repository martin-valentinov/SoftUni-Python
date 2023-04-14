annual_tax = int(input())
trainers = 0.6 * annual_tax
sports_kit = 0.8 * trainers
basketball = 0.25 * sports_kit
accessories = 0.20 * basketball

price = annual_tax + trainers + sports_kit + basketball + accessories

print(price)