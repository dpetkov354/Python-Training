# 5 Supplies for School
pen_price = float(5.80)
marker_price = float(7.20)
board_cleaner_price_per_liter = float(1.20)
pen_quantity = int(input())
marker_quantity = int(input())
board_cleaner_liters_quantity = int(input())
discount_amount = int(input())
pen_price_total = pen_price * pen_quantity
marker_price_total = marker_price * marker_quantity
board_cleaner_price_total = board_cleaner_price_per_liter * board_cleaner_liters_quantity
total_price = pen_price_total + marker_price_total + board_cleaner_price_total
percentage_constant_conversion = discount_amount / int(100)
final_price_after_discount = total_price - (total_price * percentage_constant_conversion)
print(f'Крайна цена с намеление: {final_price_after_discount} лв.')
