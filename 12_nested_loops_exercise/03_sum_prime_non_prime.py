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
