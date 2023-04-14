from math import floor
breed = input()
sex = input()
age = 0

if breed == 'British Shorthair':
    if sex == 'm':
        age = 13
    else:
        age = 14
elif breed == 'Siamese':
    if sex == 'm':
        age = 15
    else:
        age = 16
elif breed == 'Persian':
    if sex == 'm':
        age = 14
    else:
        age = 15
elif breed == 'Ragdoll':
    if sex == 'm':
        age = 16
    else:
        age = 17
elif breed == 'American Shorthair':
    if sex == 'm':
        age = 12
    else:
        age = 13
elif breed == 'Siberian':
    if sex == 'm':
        age = 11
    else:
        age = 12

months = age * 12
cat_months = months / 6

if breed == 'British Shorthair' or breed == 'Siamese' or breed == 'Persian' or breed == 'Ragdoll' or\
breed == 'American Shorthair' or breed == 'Siberian':
    print(f'{floor(cat_months)} cat months')
else:
    print(f'{breed} is invalid cat!')
