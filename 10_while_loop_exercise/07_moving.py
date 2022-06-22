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
