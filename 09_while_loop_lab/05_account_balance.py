# 5 Account balance
inpt = input()
total = 0

while inpt != "NoMoreMoney":
    money = float(inpt)
    if money < 0:
        print('Invalid operation!')
        break
    total += money
    print(f'Increase: {money:.2f}')
    inpt = input()
print(f'Total: {total:.2f}')
