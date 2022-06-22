# 5 Coins
change_dec = float(input())
change = int(change_dec * 100)
coin_count = 0
while change > 0:
    if change >= 200:
        change -= 200
        coin_count += 1
    if 200 > change >= 100:
        change -= 100
        coin_count += 1
    if 100 > change >= 50:
        change -= 50
        coin_count += 1
    if 50 > change >= 20:
        change -= 20
        coin_count += 1
    if 20 > change >= 10:
        change -= 10
        coin_count += 1
    if 10 > change >= 5:
        change -= 5
        coin_count += 1
    if 5 > change >= 2:
        change -= 2
        coin_count += 1
    if 2 > change >= 1:
        change -= 1
        coin_count += 1
print(coin_count)
