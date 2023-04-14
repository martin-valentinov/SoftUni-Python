deposited_sum = float(input())
deposit_period = int(input())
annual_interest_rate = float(input())

interest_percent = annual_interest_rate/100

sum = deposited_sum + deposit_period*(deposited_sum*interest_percent/12)

print(sum)