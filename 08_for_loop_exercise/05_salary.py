# 5 Salary
tabs = int(input())
pay = int(input())

for i in range(1, tabs + 1):
    site_name = input()
    if site_name == "Facebook":
        pay -= 150
        if pay <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Instagram":
        pay -= 100
        if pay <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Reddit":
        pay -= 50
        if pay <= 0:
            print("You have lost your salary.")
            break
    else:
        continue
if pay > 0:
    print(pay)
