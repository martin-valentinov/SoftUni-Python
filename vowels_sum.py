text = input()
sum = 0

for x in text:
    if x == 'a':
        sum += 1
    elif x == 'e':
        sum += 2
    elif x == 'i':
        sum += 3
    elif x == 'o':
        sum += 4
    elif x == 'u':
        sum += 5
print(sum)
