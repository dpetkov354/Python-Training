# 3 Vacation
trip_money = float(input())
available_money = float(input())
spend_count = 0
total_days = 0

while trip_money > available_money and spend_count < 5:
    transaction = input()
    amount = float(input())
    total_days += 1
    if transaction == "spend":
        available_money -= amount
        spend_count += 1
        if available_money < 0:
            available_money = 0
    if spend_count == 5:
        print("You can\'t save the money. ")
        print(total_days)
    if transaction == "save":
        available_money += amount
        spend_count = 0
    if available_money >= trip_money:
        print(f'You saved the money for {total_days} days.')
