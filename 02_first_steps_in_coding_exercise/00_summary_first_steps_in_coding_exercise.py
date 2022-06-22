# 1 USD to BGN
usd = float(input())
bgn = usd * 1.79549
print(bgn)

# 2 Radians to Degrees
from math import pi
radians = float(input())
degrees = radians * 180 / pi
print(degrees)

# 3 Deposit Calculator
deposited_value = float(input())
number_monthly_payments = float(input())
interest_rate = float(input())
interest_sum = deposited_value * (interest_rate / 100)
monthly_interest = interest_sum / 12
total_sum = deposited_value + (number_monthly_payments * monthly_interest)
print(f'Сума в края на срока: {total_sum} лв.')

# 4 Vacation books list
page_quantity = int(input())
pages_per_hour = int(input())
total_days_for_reading = int(input())
total_time_for_reading = int(page_quantity / pages_per_hour)
hours_per_day = int(total_time_for_reading / total_days_for_reading)
print(f'Необходими са {hours_per_day} часа на ден за четене.')

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

# 6 Repainting
nylon_price_per_sq_m = float(1.50)
paint_price_per_liter = float(14.50)
paint_thinner_price_per_liter = float(5.00)
bag_flat_price = float(0.40)
nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
man_hours = int(input())
nylon_price = float((nylon_quantity+int(2)) * nylon_price_per_sq_m)
paint_price = float((paint_quantity * float(1.1)) * paint_price_per_liter)
paint_thinner_price = float(paint_thinner_quantity * paint_thinner_price_per_liter)
total_material_price = float(nylon_price + paint_price + paint_thinner_price + bag_flat_price)
total_price_work = float((total_material_price * float(0.3)) * man_hours)
final_price = float(total_material_price + total_price_work)
print(f'Крайна сума: {final_price} лв.')

# 7 Food Delivery
chicken_menu_price = float(10.35)
fish_menu_price = float(12.40)
vegetarian_menu_price = float(8.15)
delivery_price = float(2.50)
chicken_menu_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())
total_chicken_menus_price = float(chicken_menu_price * chicken_menu_quantity)
total_fish_menu_price = float(fish_menu_price * fish_menu_quantity)
total_vegetarian_menu_price = float(vegetarian_menu_price * vegetarian_menu_quantity)
total_menu_price = float(total_chicken_menus_price + total_fish_menu_price + total_vegetarian_menu_price)
desert_price = float(total_menu_price * 0.2)
final_price = float(total_menu_price + desert_price + delivery_price)
print(f'Total price: {final_price} lv.')

# 8 Basketball Equipment
yearly_payment = int(input())
price_shoes = float(yearly_payment - float(yearly_payment * 0.4))
price_clothes = float(price_shoes - float(price_shoes * 0.2))
price_ball = float(price_clothes * 0.25)
price_accessories = float(price_ball * 0.2)
total_price = float(yearly_payment + price_accessories + price_ball + price_shoes + price_clothes)
print(f'Total yearly training expenses: {total_price} lv.')

# 9 Fish Tank
length = float(input())
width = float(input())
height = float(input())
percent = float(input())
volume_cm_cubed = float(length * width * height)
volume_liters = float(volume_cm_cubed / int(1000))
used_space = float(percent / int(100))
required_liters = float(volume_liters * float(int(1)-used_space))
print(f'{required_liters} liters of water are needed to fill up the fish tank')
