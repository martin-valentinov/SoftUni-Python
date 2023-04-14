nylon_quantity = int(input())
paint_quantity = int(input())
diluent_quantity = int(input())
hours_of_work = int(input())

nylon_price = 1.50
paint_price = 14.50
diluent_price = 5.00

nylon_quantity += 2
paint_quantity *= 1.1

expenses = nylon_quantity * nylon_price + paint_quantity * paint_price + \
    diluent_quantity * diluent_price + 0.40

price_for_an_hour_work = expenses * 0.3
expenses_for_work_total = hours_of_work * price_for_an_hour_work

expenses = expenses + expenses_for_work_total

print(expenses)


