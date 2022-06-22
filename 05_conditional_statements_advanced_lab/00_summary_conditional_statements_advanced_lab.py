# 1 Day of Week
day_of_week = int(input())
if 1 <= day_of_week <= 7:
    if day_of_week == 1:
        print("Monday")
    elif day_of_week == 2:
        print("Tuesday")
    elif day_of_week == 3:
        print("Wednesday")
    elif day_of_week == 4:
        print("Thursday")
    elif day_of_week == 5:
        print("Friday")
    elif day_of_week == 6:
        print("Saturday")
    elif day_of_week == 7:
        print("Sunday")
else:
    print("Error")

# 2 Weekend or Working Day
day_of_week = str(input())

if day_of_week == str("Monday"):
    print("Working day")
elif day_of_week == str("Tuesday"):
    print("Working day")
elif day_of_week == str("Wednesday"):
    print("Working day")
elif day_of_week == str("Thursday"):
    print("Working day")
elif day_of_week == str("Friday"):
    print("Working day")
elif day_of_week == str("Saturday"):
    print("Weekend")
elif day_of_week == str("Sunday"):
    print("Weekend")
else:
    print("Error")

# 3 Animal Type
animal = str(input())

if animal == str("dog"):
    print("mammal")
elif animal == str("crocodile"):
    print("reptile")
elif animal == str("tortoise"):
    print("reptile")
elif animal == str("snake"):
    print("reptile")
else:
    print("unknown")

# 4 Personal Titles
age = float(input())
gender = input()

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

# 5 Small Shop
product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60

elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50

elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55
print(float(price * quantity))

# 6 Number in Range
number = int(input())
if -100 <= number <= 100 and number != 0:
    print("Yes")
else:
    print("No")

# 7 Working Hours
hour = int(input())
day = input()

if 10 <= hour <= 18:
    if day == "Monday":
        print("open")
    if day == "Tuesday":
        print("open")
    if day == "Wednesday":
        print("open")
    if day == "Thursday":
        print("open")
    if day == "Friday":
        print("open")
    if day == "Saturday":
        print("open")
    if day == "Sunday":
        print("closed")
else:
    print("closed")

# 8 Cinema Ticket
day = input()
price = 0
if day == "Monday":
    price = 12
    print(price)
if day == "Tuesday":
    price = 12
    print(price)
if day == "Wednesday":
    price = 14
    print(price)
if day == "Thursday":
    price = 14
    print(price)
if day == "Friday":
    price = 12
    print(price)
if day == "Saturday":
    price = 16
    print(price)
if day == "Sunday":
    price = 16
    print(price)

# 9 Fruit or Vegetable
food = input()

if food == "banana" or food == "apple" or food == "kiwi" or food == "cherry" or food == "lemon" or food == "grapes":
    print("fruit")
elif food == "tomato" or food == "cucumber" or food == "pepper" or food == "carrot":
    print("vegetable")
else:
    print("unknown")

# 10 Invalid Number
number = int(input())

if 100 > number or number > 200:
    if number != 0:
        print("invalid")

# 11 Fruit Shop
fruit = input()
dotw = input()
qty = float(input())
price = 0

if dotw == "Saturday" or dotw == "Sunday":
    if fruit == "banana":
        price = 2.70
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "apple":
        price = 1.25
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "orange":
        price = 0.90
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "grapefruit":
        price = 1.60
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "kiwi":
        price = 3.00
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "pineapple":
        price = 5.60
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "grapes":
        price = 4.20
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    else:
        print("error")
elif dotw == "Monday" or dotw == "Tuesday" or dotw == "Wednesday" or dotw == "Thursday" or dotw == "Friday":
    if fruit == "banana":
        price = 2.50
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "apple":
        price = 1.20
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "orange":
        price = 0.85
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "grapefruit":
        price = 1.45
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "kiwi":
        price = 2.70
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "pineapple":
        price = 5.50
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    elif fruit == "grapes":
        price = 3.85
        f_price = float(price * qty)
        tf_price = "{:.2f}".format(f_price)
        print(tf_price)
    else:
        print("error")
else:
    print("error")

# 12 Trade Commissions
city = input()
sales = float(input())
commission = 0

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = sales * 0.05
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.045
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.055
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = sales * 0.07
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.075
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.08
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = sales * 0.08
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.1
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.12
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
elif sales > 10000:
    if city == "Sofia":
        commission = sales * 0.12
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Varna":
        commission = sales * 0.13
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    elif city == "Plovdiv":
        commission = sales * 0.145
        ref_comm = "{:.2f}".format(commission)
        print(ref_comm)
    else:
        print("error")
else:
    print("error")
