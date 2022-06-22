# 4 Vacation books list
page_quantity = int(input())
pages_per_hour = int(input())
total_days_for_reading = int(input())
total_time_for_reading = int(page_quantity / pages_per_hour)
hours_per_day = int(total_time_for_reading / total_days_for_reading)
print(f'Необходими са {hours_per_day} часа на ден за четене.')