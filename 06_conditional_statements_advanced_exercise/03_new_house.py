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
