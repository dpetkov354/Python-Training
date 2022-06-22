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
