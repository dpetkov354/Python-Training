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
