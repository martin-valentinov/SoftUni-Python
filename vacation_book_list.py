book_pages = int(input())
pages_per_hour = int(input())
days_to_complete = int(input())

hours_to_read = book_pages / pages_per_hour

hours_per_day = hours_to_read / days_to_complete

print(int(hours_per_day))