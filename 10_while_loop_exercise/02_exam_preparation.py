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
