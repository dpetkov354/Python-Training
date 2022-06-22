# 1 Sum Seconds
import math

first = int(input())
second = int(input())
third = int(input())

total_time = first + second + third
minutes = total_time // 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')

# 2 Bonus Score
points = int(input("Enter bonus points:"))
bonus = 0

if points <= 100:
    bonus = bonus + 5
elif points > 1000:
    bonus = points * 0.1
else:
    bonus = points * 0.2

if points % 2 == 0:
    bonus = bonus + 1
elif points % 5 == 0:
    bonus = bonus + 2

print(f'Total bonus is:', bonus)
print(f'Total points plus bonus is:', (bonus + points))

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

# 4 Toy Shop
trip_cost = float(input())
puzzle_quantity = int(input())
dolls_quantity = int(input())
bears_quantity = int(input())
minions_quantity = int(input())
trucks_quantity = int(input())

total_quantity = puzzle_quantity + dolls_quantity + bears_quantity + minions_quantity + trucks_quantity
total_price = (puzzle_quantity * 2.60) + (dolls_quantity * 3.00) + (bears_quantity * 4.10) + (minions_quantity * 8.20) + (trucks_quantity * 2.00)

if total_quantity >= 50:
    total_price = total_price * 0.75
    total_price = total_price * 0.90
    if total_price >= trip_cost:
        print(f'Yes! %.2f lv left.' % (total_price - trip_cost))
    elif total_price <= trip_cost:
        print(f'Not enough money! %.2f lv needed.' % (trip_cost - total_price))

elif total_quantity < 50:
    total_price = total_price * 0.90
    if total_price >= trip_cost:
        print(f'Yes! %.2f lv left.' % (total_price - trip_cost))
    elif total_price <= trip_cost:
        print(f'Not enough money! %.2f lv needed.' % (trip_cost - total_price))


# 5 Godzilla vs. Kong
budget = float(input())
number_extras = int(input())
price_extra = float(input())

decor_price = budget * 0.1
if number_extras >= 150:
    total_price_extra = (number_extras * price_extra) * 0.9
else:
    total_price_extra = number_extras * price_extra

total_film_cost = decor_price + total_price_extra

if total_film_cost <= budget:
    print('Action!')
    print(f'Wingard starts filming with %.2f leva left.' % (budget - total_film_cost))
elif total_film_cost > budget:
    print('Not enough money!')
    print(f'Wingard needs %.2f leva more.' % (total_film_cost - budget))

# 6 World Swimming Record
import math

record_current = float(input())
distance_to_swim = float(input())
time_1meter = float(input())

swim_time = distance_to_swim * time_1meter
delay_swim_time = math.floor(distance_to_swim / 15) * 12.5
tot_swim_time = round((swim_time + delay_swim_time), 2)

if tot_swim_time < record_current:
    print(f'Yes, he succeeded! The new world record is %.2f seconds.' % tot_swim_time)
elif tot_swim_time >= record_current:
    print(f'No, he failed! He was %.2f seconds slower.' % (tot_swim_time - record_current))

# 7 Shopping
budget = float(input())
grph_card_number = int(input())
proc_number = int(input())
ram_mem_number = int(input())

price_grph_card = grph_card_number * 250
price_proc = (0.35 * price_grph_card) * proc_number
price_ram_mem = (0.1 * price_grph_card) * ram_mem_number

total_price = price_proc + price_ram_mem + price_grph_card

if grph_card_number > proc_number:
    total_price = total_price * 0.85

if budget >= total_price:
    print(f'You have %.2f leva left!' % (budget - total_price))
elif budget < total_price:
    print(f'Not enough money! You need %.2f leva more!' % (total_price - budget))

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
