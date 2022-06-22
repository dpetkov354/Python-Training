# 1 Old Books
book_name = input()
book_count = 0
is_book_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f'You checked {book_count} books and found it.')
        break
    book_count += 1
    current_book = input()
if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')

# 2 Exam Preparation
number_bad_grades = int(input())
avg_score = 0
sum_problems = 0
solved_problems = 0
failed_problems = 0
last_problem = ''
has_failed = False

while failed_problems < number_bad_grades:
    name_problem = input()
    if name_problem == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_problems += 1
    if failed_problems >= number_bad_grades:
        has_failed = True
        break
    sum_problems += grade
    solved_problems += 1
    last_problem = name_problem

if has_failed:
    print(f"You need a break, {number_bad_grades} poor grades.")
else:
    print(f'Average score: {sum_problems / solved_problems:.2f}')
    print(f'Number of problems: {solved_problems}')
    print(f'Last problem: {last_problem}')

# 3 Vacation
trip_money = float(input())
available_money = float(input())
spend_count = 0
total_days = 0

while trip_money > available_money and spend_count < 5:
    transaction = input()
    amount = float(input())
    total_days += 1
    if transaction == "spend":
        available_money -= amount
        spend_count += 1
        if available_money < 0:
            available_money = 0
    if spend_count == 5:
        print("You can\'t save the money. ")
        print(total_days)
    if transaction == "save":
        available_money += amount
        spend_count = 0
    if available_money >= trip_money:
        print(f'You saved the money for {total_days} days.')

# 4 Walking
target_steps = 10000
walked_steps = 0
going_home = False

while not going_home:
    initial_inp = input()
    if initial_inp != 'Going home':
        walked_steps += int(initial_inp)
        if walked_steps > target_steps:
            going_home = True
    else:
        walked_steps += int(input())
        going_home = True
if target_steps > walked_steps:
    print(f'{target_steps - walked_steps} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{walked_steps - target_steps} steps over the goal!')

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

# 6 Cake
cake_length = int(input())
cake_width = int(input())
cake_surface = cake_width * cake_length
command_stop = False

while not command_stop and cake_surface > 0:
    order = input()
    if order != "STOP":
        cake_surface -= int(order)
        continue
    else:
        break

if cake_surface > 0:
    print(f'{cake_surface} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_surface)} pieces more.')

# 7 Moving
house_length = int(input())
house_width = int(input())
house_height = int(input())
house_volume = house_width * house_length * house_height
command_done = False

while not command_done and house_volume > 0:
    command = input()
    if command != "Done":
        house_volume -= int(command)
        continue
    else:
        break

if house_volume > 0:
    print(f'{house_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(house_volume)} Cubic meters more.')
