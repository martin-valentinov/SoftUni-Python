square_metres = float(input())
price_per_square_metre = 7.61
price = square_metres * price_per_square_metre
discount = price * 0.18
final_price = price - discount
print(f'The final price is {final_price} lv.')
print(f'The discount is {discount} lv.')
