# 8 Lunch Break
import math
name_show = str(input())
show_duration = int(input())
lunch_break_duration = int(input())

time_lunch = lunch_break_duration / 8
rest_duration = lunch_break_duration / 4
remaining_time = lunch_break_duration - time_lunch - rest_duration

if remaining_time >= show_duration:
    print(f'You have enough time to watch {name_show} and left with {math.ceil(remaining_time - show_duration)} minutes free time.')
elif remaining_time < show_duration:
    print(f'You don\'t have enough time to watch {name_show}, you need {math.ceil(show_duration - remaining_time)} more minutes.')
