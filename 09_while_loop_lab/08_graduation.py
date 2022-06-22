# 8 Graduation
student_name = input()
count_grade = 0
sum_grade = 0.0
no_pass = 0

while count_grade < 12:
    grade = float(input())
    if grade < 4.00:
        no_pass += 1
        if no_pass > 1:
            print(f'{student_name} has been excluded at {(count_grade + 1)} grade')
            break
        continue
    sum_grade += grade
    count_grade += 1
average = sum_grade / 12
if no_pass != 2:
    print(f'{student_name} graduated. Average grade: {average:.02f}')
