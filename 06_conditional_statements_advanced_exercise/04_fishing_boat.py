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
