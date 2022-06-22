# 1 Read Text
while True:
    name = input()
    if name == "Stop":
        break
    print(name)

# 2 Password
name = input()
password = input()

while True:
    data = input()
    if data != password:
        continue
    elif data == password:
        print(f'Welcome {name}!')
        break

# 3 Sum Numbers
num = int(input())
data = 0

while True:
    data += int(input())
    if data >= num:
        print(data)
        break
    else:
        continue

# 4 Sequence 2k+1
num = int(input())
data = 1

while data <= num:
    print(data)
    data = data * 2 + 1

# 5 Account balance
inpt = input()
total = 0

while inpt != "NoMoreMoney":
    money = float(inpt)
    if money < 0:
        print('Invalid operation!')
        break
    total += money
    print(f'Increase: {money:.2f}')
    inpt = input()
print(f'Total: {total:.2f}')

# 6 Max Number
inpt = input()
largest = -100000000000000000000000000

while inpt != "Stop":
    money = int(inpt)
    if money > largest:
        largest = money
    inpt = input()
print(largest)

# 7 Min Number
inpt = input()
smallest = 100000000000000000000000000

while inpt != "Stop":
    money = int(inpt)
    if money < smallest:
        smallest = money
    inpt = input()
print(smallest)

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
