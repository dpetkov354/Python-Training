# 1 Cinema
ticket_type = input()
rows = int(input())
columns = int(input())
revenue = 0

cinema_capacity = rows * columns

if ticket_type == "Premiere":
    revenue = cinema_capacity * 12.00
elif ticket_type == "Normal":
    revenue = cinema_capacity * 7.50
elif ticket_type == "Discount":
    revenue = cinema_capacity * 5.00
print(f'{revenue:.2f} leva')

# 2 Summer Outfit
temp = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= temp <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temp <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= temp <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temp <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_day == "Evening":
    if 10 <= temp <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temp <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f'It\'s {temp} degrees, get your {outfit} and {shoes}.')

# 3 New House
flowers = input()
num_flowers = int(input())
budget = int(input())
price_per_flower = 0
total_price = 0
left_money = 0

if flowers == "Roses":
    price_per_flower = 5.00
    if num_flowers > 80:
        total_price = (price_per_flower * num_flowers) * 0.9
    else:
        total_price = (price_per_flower * num_flowers)
elif flowers == "Dahlias":
    price_per_flower = 3.80
    if num_flowers > 90:
        total_price = (price_per_flower * num_flowers) * 0.85
    else:
        total_price = (price_per_flower * num_flowers)
elif flowers == "Tulips":
    price_per_flower = 2.80
    if num_flowers > 80:
        total_price = (price_per_flower * num_flowers) * 0.85
    else:
        total_price = (price_per_flower * num_flowers)
elif flowers == "Narcissus":
    price_per_flower = 3.00
    if num_flowers < 120:
        total_price = (price_per_flower * num_flowers) * 1.15
    else:
        total_price = (price_per_flower * num_flowers)
elif flowers == "Gladiolus":
    price_per_flower = 2.50
    if num_flowers < 80:
        total_price = (price_per_flower * num_flowers) * 1.2
    else:
        total_price = (price_per_flower * num_flowers)
else:
    quit()
if budget >= total_price:
    print(f'Hey, you have a great garden with {num_flowers} {flowers} and {(budget - total_price):.2f} leva left.')
else:
    print(f"Not enough money, you need {(total_price - budget):.2f} leva more.")

# 4 Fishing Boat
budget = int(input())
season = input()
num_fisherman = int(input())
boat_price = 0

if season == "Spring":
    boat_price = 3000
    if num_fisherman <= 6:
        boat_price = boat_price * 0.9
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
    elif 7 < num_fisherman <= 11:
        boat_price = boat_price * 0.85
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
    elif num_fisherman >= 12:
        boat_price = boat_price * 0.75
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
if season == "Autumn":
    boat_price = 4200
    if num_fisherman <= 6:
        boat_price = boat_price * 0.9
    elif 7 < num_fisherman <= 11:
        boat_price = boat_price * 0.85
    elif num_fisherman >= 12:
        boat_price = boat_price * 0.75
if season == "Summer":
    boat_price = 4200
    if num_fisherman <= 6:
        boat_price = boat_price * 0.9
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
    elif 7 < num_fisherman <= 11:
        boat_price = boat_price * 0.85
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
    elif num_fisherman >= 12:
        boat_price = boat_price * 0.75
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
if season == "Winter":
    boat_price = 2600
    if num_fisherman <= 6:
        boat_price = boat_price * 0.9
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
    elif 7 < num_fisherman <= 11:
        boat_price = boat_price * 0.85
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
    elif num_fisherman >= 12:
        boat_price = boat_price * 0.75
        if (num_fisherman % 2) == 0:
            boat_price = boat_price * 0.95
if budget >= boat_price:
    print(f'Yes! You have {(budget - boat_price):.2f} leva left.')
else:
    print(f"Not enough money! You need {(boat_price - budget):.2f} leva.")

# 5 Journey
budget = float(input())
season = input()
destination = ""
rest_price = 0
type_place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        rest_price = budget * 0.3
        type_place = "Camp"
    elif season == "winter":
        rest_price = budget * 0.7
        type_place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        rest_price = budget * 0.4
        type_place = "Camp"
    elif season == "winter":
        rest_price = budget * 0.8
        type_place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    rest_price = budget * 0.9
    type_place = "Hotel"

print(f'Somewhere in {destination}')
if season != "":
    print(f"{type_place} " '-' f" {rest_price:.2f}")

# 6 Operations Between
n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    if ((n1 + n2) % 2) == 0:
        print(f'{n1} + {n2} = {n1 + n2} - even')
    elif ((n1 + n2) % 2) != 0:
        print(f'{n1} + {n2} = {n1 + n2} - odd')
elif operator == "-":
    if ((n1 - n2) % 2) == 0:
        print(f'{n1} - {n2} = {n1 - n2} - even')
    elif ((n1 - n2) % 2) != 0:
        print(f'{n1} - {n2} = {n1 - n2} - odd')
elif operator == "*":
    if ((n1 * n2) % 2) == 0:
        print(f'{n1} * {n2} = {n1 * n2} - even')
    elif ((n1 * n2) % 2) != 0:
        print(f'{n1} * {n2} = {n1 * n2} - odd')
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        dev_res = n1 / n2
        print(f'{n1} / {n2} = {dev_res:.2f} ')
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        dev_res = n1 % n2
        print(f'{n1} % {n2} = {dev_res} ')

# 7 Hotel Room
month = input()
nights = int(input())
price_night_studio = 0
price_night_apart = 0

if month == "May" or month == "October":
    if nights <= 7:
        price_night_studio = 50
        price_night_apart = 65
        print(f'Apartment: {(price_night_apart * nights):.2f} lv.')
        print(f'Studio: {(price_night_studio * nights):.2f} lv.')
    elif 14 >= nights >= 8:
        price_night_studio = 50
        price_night_apart = 65
        print(f'Apartment: {(price_night_apart * nights):.2f} lv.')
        print(f'Studio: {((price_night_studio * nights) * 0.95):.2f} lv.')
    elif nights > 14:
        price_night_studio = 50
        price_night_apart = 65
        print(f'Apartment: {((price_night_apart * nights) * 0.9):.2f} lv.')
        print(f'Studio: {((price_night_studio * nights) * 0.7):.2f} lv.')
if month == "June" or month == "September":
    if nights <= 7:
        price_night_studio = 75.20
        price_night_apart = 68.70
        print(f'Apartment: {(price_night_apart * nights):.2f} lv.')
        print(f'Studio: {(price_night_studio * nights):.2f} lv.')
    elif 14 >= nights >= 8:
        price_night_studio = 75.20
        price_night_apart = 68.70
        print(f'Apartment: {(price_night_apart * nights):.2f} lv.')
        print(f'Studio: {(price_night_studio * nights):.2f} lv.')
    elif nights > 14:
        price_night_studio = 75.20
        price_night_apart = 68.70
        print(f'Apartment: {((price_night_apart * nights) * 0.9):.2f} lv.')
        print(f'Studio: {((price_night_studio * nights) * 0.8):.2f} lv.')
if month == "July" or month == "August":
    if nights <= 7:
        price_night_studio = 76
        price_night_apart = 77
        print(f'Apartment: {(price_night_apart * nights):.2f} lv.')
        print(f'Studio: {(price_night_studio * nights):.2f} lv.')
    elif 14 >= nights >= 8:
        price_night_studio = 76
        price_night_apart = 77
        print(f'Apartment: {(price_night_apart * nights):.2f} lv.')
        print(f'Studio: {(price_night_studio * nights):.2f} lv.')
    elif nights > 14:
        price_night_studio = 76
        price_night_apart = 77
        print(f'Apartment: {((price_night_apart * nights) * 0.9):.2f} lv.')
        print(f'Studio: {(price_night_studio * nights):.2f} lv.')

# 8 On Time for the Exam
exam_hour = int(input())
exam_minutes = int(input())
exam_time_minutes = (exam_hour * 60) + exam_minutes
arrival_hour = int(input())
arrival_minutes = int(input())
arrival_time_minutes = (arrival_hour * 60) + arrival_minutes
diff_minutes = abs(exam_time_minutes - arrival_time_minutes)
hours = diff_minutes // 60
minutes = diff_minutes % 60
if 23 >= exam_hour >= 0 and 59 >= exam_minutes >= 0 and 23 >= arrival_hour >= 0 and 59 >= arrival_minutes >= 0:
    if exam_hour == arrival_hour and exam_minutes == arrival_minutes:
        print("On time")
    elif exam_time_minutes > arrival_time_minutes and diff_minutes <= 30:
        print("On time")
        print(f'{minutes} minutes before the start')
    if exam_time_minutes > arrival_time_minutes and 60 > diff_minutes > 30:
        print("Early")
        print(f'{minutes} minutes before the start')
    elif exam_time_minutes > arrival_time_minutes and diff_minutes >= 60:
        print("Early")
        print(f'{hours}:{minutes:02d} hours before the start')
    if exam_time_minutes < arrival_time_minutes and 60 > abs(diff_minutes) >= 1:
        print("Late")
        print(f'{abs(minutes)} minutes after the start')
    elif exam_time_minutes < arrival_time_minutes and abs(diff_minutes) >= 60:
        print("Late")
        print(f'{abs(hours)}:{(abs(minutes)):02d} hours after the start')
else:
    quit()

# 9 Ski Trip
days = int(input())
type_of_room = input()
grade = input()
price = 0

if type_of_room == "room for one person":
    price = (days - 1) * 18.00
    if grade == "positive":
        price = price * 1.25
    else:
        price = price * 0.9
    print(f'{price:0.2f}')
if type_of_room == "apartment":
    price = (days - 1) * 25.00
    if days < 10:
        price = price * 0.7
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if 10 <= days <= 15:
        price = price * 0.65
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if days > 15:
        price = price * 0.5
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
if type_of_room == "president apartment":
    price = (days - 1) * 35.00
    if days < 10:
        price = price * 0.9
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if 10 <= days <= 15:
        price = price * 0.85
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
    if days > 15:
        price = price * 0.8
        if grade == "positive":
            price = price * 1.25
        else:
            price = price * 0.9
        print(f'{price:0.2f}')
