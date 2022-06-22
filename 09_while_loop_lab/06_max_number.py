# 6 Max Number
inpt = input()
largest = -100000000000000000000000000

while inpt != "Stop":
    money = int(inpt)
    if money > largest:
        largest = money
    inpt = input()
print(largest)
