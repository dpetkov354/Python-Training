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
