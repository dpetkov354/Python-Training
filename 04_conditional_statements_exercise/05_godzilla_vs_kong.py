# 5 Godzilla vs. Kong
budget = float(input())
number_extras = int(input())
price_extra = float(input())

decor_price = budget * 0.1
if number_extras >= 150:
    total_price_extra = (number_extras * price_extra) * 0.9
else:
    total_price_extra = number_extras * price_extra

total_film_cost = decor_price + total_price_extra

if total_film_cost <= budget:
    print('Action!')
    print(f'Wingard starts filming with %.2f leva left.' % (budget - total_film_cost))
elif total_film_cost > budget:
    print('Not enough money!')
    print(f'Wingard needs %.2f leva more.' % (total_film_cost - budget))
