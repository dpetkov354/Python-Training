# 1 Area of figures
from math import pi as pi

figure_type = input()
if figure_type == 'square':
    a = float(input())
    print(f"{pow(a, 2):.3f}")
elif figure_type == 'rectangle':
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif figure_type == 'circle':
    r = float(input())
    print(f"{pi * pow(r, 2):.3f}")
elif figure_type == 'triangle':
    a = float(input())
    b = float(input())
    print(f"{a * b / 2:.3f}")

# 2 Even or Odd
test_num = int(input())
if test_num % 2 > 0:
    print('odd')
else:
    print('even')

# 3 Excellent Score
score = float(input())
if score >= 5.50:
    print('Excellent!')

# 4 Number 100 - 200

num = int(input())
if 100 <= num <= 200:
    print('Between 100 and 200')
elif num <= 100:
    print('Less than 100')
else:
    print('Greater than 200')

# 5 Password guess
password = input()
correct = "s3cr3t!P@ssw0rd"
if password == correct:
    print("Welcome")
else:
    print("Wrong password!")

# 6 Speed info
speed = float(input())
if speed <= 10:
    print('slow')
elif 10 < speed <= 50:
    print('average')
elif 50 < speed <= 150:
    print('fast')
elif 150 < speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
