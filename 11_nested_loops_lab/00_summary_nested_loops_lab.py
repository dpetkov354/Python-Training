# 1 Clock
for h in range(24):
    for m in range(60):
        print(f"{h}:{m}")

# 2 Multiplication Table
for x in range(1, 11):
    for y in range(1, 11):
        product = x * y
        print(f"{x} * {y} = {product}")

# 3 Combinations
needed_result = int(input())
count = 0

for x1 in range(needed_result + 1):
    for x2 in range(needed_result + 1):
        for x3 in range(needed_result + 1):
            if (x1 + x2 + x3) == needed_result:
                count += 1
print(count)

# 4 Sum of Two Numbers
start = int(input())
finish = int(input())
magic_number = int(input())
count = 0
stop = False

for i in range(start, finish + 1):
    for n in range(start, finish + 1):
        count += 1
        if i + n == magic_number:
            print(f'Combination N:{count} ({i} + {n} = {magic_number})')
            stop = True
            break
    if stop:
        break
else:
    print(f'{count} combinations - neither equals {magic_number}')

# 5 Travelling
trip_end = False

while not trip_end:
    destination = input()
    if destination == "End":
        trip_end = True
        break
    input_min_cost = input()
    if input_min_cost == "End":
        trip_end = True
        break
    else:
        min_cost = float(input_min_cost)
        while min_cost > 0:
            deposit = float(input())
            min_cost -= deposit
        print(f"Going to {destination}!")

# 6 Building
floors = int(input())
living_space = int(input())
for i in range(floors, 0, -1):
    for n in range(0, living_space):
        if i == floors:
            print("L{0}{1}".format(i, n), end=" ")
        elif i % 2 == 0:
            print("O{0}{1}".format(i, n), end=" ")
        else:
            print("A{0}{1}".format(i, n), end=" ")
    print("")
