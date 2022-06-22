# 4 Walking
target_steps = 10000
walked_steps = 0
going_home = False

while not going_home:
    initial_inp = input()
    if initial_inp != 'Going home':
        walked_steps += int(initial_inp)
        if walked_steps > target_steps:
            going_home = True
    else:
        walked_steps += int(input())
        going_home = True
if target_steps > walked_steps:
    print(f'{target_steps - walked_steps} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{walked_steps - target_steps} steps over the goal!')
