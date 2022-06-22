# 7 Min Number
inpt = input()
smallest = 100000000000000000000000000

while inpt != "Stop":
    money = int(inpt)
    if money < smallest:
        smallest = money
    inpt = input()
print(smallest)
