# 7 Shopping
budget = float(input())
grph_card_number = int(input())
proc_number = int(input())
ram_mem_number = int(input())

price_grph_card = grph_card_number * 250
price_proc = (0.35 * price_grph_card) * proc_number
price_ram_mem = (0.1 * price_grph_card) * ram_mem_number

total_price = price_proc + price_ram_mem + price_grph_card

if grph_card_number > proc_number:
    total_price = total_price * 0.85

if budget >= total_price:
    print(f'You have %.2f leva left!' % (budget - total_price))
elif budget < total_price:
    print(f'Not enough money! You need %.2f leva more!' % (total_price - budget))
