# 8 Basketball Equipment
yearly_payment = int(input())
price_shoes = float(yearly_payment - float(yearly_payment * 0.4))
price_clothes = float(price_shoes - float(price_shoes * 0.2))
price_ball = float(price_clothes * 0.25)
price_accessories = float(price_ball * 0.2)
total_price = float(yearly_payment + price_accessories + price_ball + price_shoes + price_clothes)
print(f'Total yearly training expenses: {total_price} lv.')
