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
