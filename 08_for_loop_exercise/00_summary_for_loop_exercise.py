# 1 Numbers Ending in 7
for num in range(7, 1001, 10):
    print(num)

# 2 Half Sum Element
import sys
max_num = -sys.maxsize
sum_numbers = 0
n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

if max_num == (sum_numbers - max_num):
    print("Yes")
    print(f"Sum = {sum_numbers - max_num}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_numbers)}")

# 3 Histogram
count_number = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, count_number):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    else:
        p5 += 1
print(f'{((p1/count_number)*100):.2f}%')
print(f'{((p2/count_number)*100):.2f}%')
print(f'{((p3/count_number)*100):.2f}%')
print(f'{((p4/count_number)*100):.2f}%')
print(f'{((p5/count_number)*100):.2f}%')

# 4 Clever Lily
age = int(input())
price_wm = float(input())
price_toy = int(input())
toy_count = 0
money_count = 0
brother_cut = 0
money_sum = 0
if 1 <= age <= 77:
    if 0 <= price_toy <= 40:
        for i in range(1, age + 1):
            if i % 2 == 0:
                money_count += 10
                money_sum += money_count
                brother_cut += 1
            else:
                toy_count += price_toy

        savings = (money_sum + toy_count) - brother_cut

        if savings >= price_wm:
            print(f'Yes! {(savings - price_wm):.2f}')
        else:
            print(f'No! {abs(savings - price_wm):.2f}')

    else:
        quit()
else:
    quit()

# 5 Salary
tabs = int(input())
pay = int(input())

for i in range(1, tabs + 1):
    site_name = input()
    if site_name == "Facebook":
        pay -= 150
        if pay <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Instagram":
        pay -= 100
        if pay <= 0:
            print("You have lost your salary.")
            break
    elif site_name == "Reddit":
        pay -= 50
        if pay <= 0:
            print("You have lost your salary.")
            break
    else:
        continue
if pay > 0:
    print(pay)

# 6 Oscars
name_actor = input()
points = float(input())
num_of_graders = int(input())
sum_points = points

for i in range(0, num_of_graders):
    name_grader = input()
    grade = float(input())
    letters = len(name_grader)
    sum_points += (letters * grade)/2
    if sum_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {sum_points:.1f}!")
        break
    else:
        continue
if sum_points < 1250.5:
    print(f"Sorry, {name_actor} you need {(1250.5 - sum_points):.1f} more!")

# 7 Trekking Mania
trekker_groups = int(input())
sum_trekkers = 0
musala_num = 0
montblanc_num = 0
kilimandjaro_num = 0
k2_num = 0
everest_num = 0

for i in range(0, trekker_groups):
    num_of_trekkers = int(input())
    sum_trekkers += num_of_trekkers
    if num_of_trekkers <= 5:
        musala_num += num_of_trekkers
    elif 6 <= num_of_trekkers <= 12:
        montblanc_num += num_of_trekkers
    elif 13 <= num_of_trekkers <= 25:
        kilimandjaro_num += num_of_trekkers
    elif 26 <= num_of_trekkers <= 40:
        k2_num += num_of_trekkers
    elif 41 <= num_of_trekkers:
        everest_num += num_of_trekkers
print(f'{((musala_num / sum_trekkers) * 100):.2f}%')
print(f'{((montblanc_num / sum_trekkers) * 100):.2f}%')
print(f'{((kilimandjaro_num / sum_trekkers) * 100):.2f}%')
print(f'{((k2_num / sum_trekkers) * 100):.2f}%')
print(f'{((everest_num / sum_trekkers) * 100):.2f}%')

# 8 Tennis Rank list
tournaments = int(input())
initial_points = int(input())
fin_points = initial_points
average_points = 0
win_rate = 0

for i in range(0, tournaments):
    type_of_t = input()
    if type_of_t == "W":
        fin_points += 2000
        average_points += 2000
        win_rate += 1
    elif type_of_t == "F":
        fin_points += 1200
        average_points += 1200
    elif type_of_t == "SF":
        fin_points += 720
        average_points += 720
print(f"Final points: {fin_points}")
print(f"Average points: {int(average_points / tournaments)}")
print(f"{((win_rate / tournaments) * 100):0.2f}%")
