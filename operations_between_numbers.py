n1 = int(input())
n2 = int(input())
operator = input()
total = 0
number = ''

if n2 == 0 and (operator == '/' or operator == '%'):
    print(f'Cannot divide {n1} by zero')
elif operator == '+':
    total = n1 + n2
elif operator == '-':
    total = n1 - n2
elif operator == '*':
    total = n1 * n2
elif operator == '/':
    total = n1 / n2
elif operator == '%':
    total = n1 % n2

if not operator == '%':
    if total % 2 == 0:
        number = 'even'
    else:
        number = 'odd'

if operator == '+' or operator == '-' or operator == '*':
    print(f'{n1} {operator} {n2} = {total} - {number}')
elif operator == '/' and n2 != 0:
    print(f'{n1} / {n2} = {total:.2f}')
elif operator == '%' and n2 != 0:
    print(f'{n1} % {n2} = {total}')


