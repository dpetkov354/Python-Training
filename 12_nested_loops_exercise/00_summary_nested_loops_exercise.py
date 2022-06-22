# 1 Number Pyramid
n = int(input())
current = 1
is_current_bigger_than_n = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current > n:
            is_current_bigger_than_n = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if is_current_bigger_than_n:
        break
    print()

# 2 Equal Sums Even Odd
first = int(input())
second = int(input())

for number in range(first, second + 1):
    num_to_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=' ')

# 3 Sum Prime Non Prime
stop_command = False
prime_sum = 0
non_prime_sum = 0

while not stop_command:
    command = input()
    if command == "stop":
        stop_command = True
        break
    number = int(command)
    if number < 0:
        print("Number is negative.")
        continue
    if number == 0 or number == 2 or number == 3 or number == 5 or number == 7:
        prime_sum += number
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        non_prime_sum += number
    elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        prime_sum += number
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

# 4 Train The Trainers
number_of_jury = int(input())
total_avg = 0
score_count = 0
finish = False

while not finish:
    name_of_presentation = input()
    current_avg = 0
    if name_of_presentation == 'Finish':
        finish = True
        break
    for i in range(0, number_of_jury):
        score_per_jury = float(input())
        score_count += 1
        current_avg += score_per_jury
    total_avg += current_avg
    print(f"{name_of_presentation} - {(current_avg / number_of_jury):.2f}.")
print(f"Student\'s final assessment is {(total_avg / score_count):.2f}.")

# 5 Special Numbers
number = int(input())

for n in range(1111, 9999 + 1):
    n = str(n)
    if n[0] != "0" and n[1] != "0" and n[2] != "0" and n[3] != "0":
        if number % int(n[0]) == 0 and number % int(n[1]) == 0 and number % int(n[2]) == 0 and number % int(n[3]) == 0:
            print(n, end=" ")

# 6 Cinema Tickets
name_break = False
student_count = 0
standard_count = 0
kid_count = 0
total_tickets = 0

while not name_break:
    name = input()
    if name == "Finish":
        name_break = True
        break
    movie_tickets = 0
    free_seats = int(input())
    for seats in range(0, free_seats):
        type_seat = input()
        if type_seat == 'student':
            student_count += 1
            movie_tickets += 1
            total_tickets += 1
        elif type_seat == 'standard':
            standard_count += 1
            movie_tickets += 1
            total_tickets += 1
        elif type_seat == 'kid':
            kid_count += 1
            movie_tickets += 1
            total_tickets += 1
        else:
            break
    print(f'{name} - {((movie_tickets / free_seats) * 100):.2f}% full.')
print(f'Total tickets: {total_tickets}')
print(f'{((student_count / total_tickets) *100):.2f}% student tickets.')
print(f'{((standard_count / total_tickets) *100):.2f}% standard tickets.')
print(f'{((kid_count / total_tickets) *100):.2f}% kids tickets.')
