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
