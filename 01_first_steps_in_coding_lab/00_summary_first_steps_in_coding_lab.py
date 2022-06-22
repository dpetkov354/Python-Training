# 1 Hello World
print('Hello SoftUni')

# 2 Nums 1...10
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# 3 Rectangle Area
a = int(input())
b = int(input())
area = a * b
print(area)

# 4 Inches to Centimeters
inches = float(input())
centimeters = inches * 2.54
print(centimeters)

# 5 Greeting by Name
name = input()
print(f'Hello, {name}!')

# 6 Concatenate Data
first_name = input()
last_name = input()
age = int(input())
town = input()
print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')

# 7 Projects Creation
name = input()
number_of_projects = int(input())
hours = number_of_projects*3
print(f'The architect {name} will need {hours} hours to complete {number_of_projects} project/s.')

# 8 Pet Shop
dog_food_quantity = int(input())
cat_food_quantity = int(input())
dog_food_price = float(2.50)
cat_food_price = int(4)
dog_food_total = dog_food_price*dog_food_quantity
cat_food_total = cat_food_price*cat_food_quantity
total = dog_food_total+cat_food_total
print(f'{total} lv.')


