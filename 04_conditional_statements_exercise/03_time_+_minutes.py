# 3 Time + 15 Minutes
import math
inp_hours = int(input())
inp_minutes = int(input())

if (23 >= inp_hours >= 0) and (59 >= inp_minutes >= 0):
    inp_minutes = inp_minutes + 15
    total_time = (inp_hours * 60) + inp_minutes
    hours = total_time // 60
    minutes = total_time % 60
    hours = math.floor(hours)
    if hours == 24:
        if minutes < 10:
            print(f'{hours - 24}:0{minutes}')
        elif minutes >= 10:
            print(f'{hours - 24}:{minutes}')
    elif hours != 24:
        if minutes < 10:
            print(f'{hours}:0{minutes}')
        elif minutes >= 10:
            print(f'{hours}:{minutes}')
else:
    print('Chose hours between 0 and 23 and minutes between 0 and 59')
