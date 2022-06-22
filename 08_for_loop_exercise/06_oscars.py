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
