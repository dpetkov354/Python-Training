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
