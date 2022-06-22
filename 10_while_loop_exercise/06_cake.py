# 6 Cake
cake_length = int(input())
cake_width = int(input())
cake_surface = cake_width * cake_length
command_stop = False

while not command_stop and cake_surface > 0:
    order = input()
    if order != "STOP":
        cake_surface -= int(order)
        continue
    else:
        break

if cake_surface > 0:
    print(f'{cake_surface} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_surface)} pieces more.')
