# 6 Operations Between
n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    if ((n1 + n2) % 2) == 0:
        print(f'{n1} + {n2} = {n1 + n2} - even')
    elif ((n1 + n2) % 2) != 0:
        print(f'{n1} + {n2} = {n1 + n2} - odd')
elif operator == "-":
    if ((n1 - n2) % 2) == 0:
        print(f'{n1} - {n2} = {n1 - n2} - even')
    elif ((n1 - n2) % 2) != 0:
        print(f'{n1} - {n2} = {n1 - n2} - odd')
elif operator == "*":
    if ((n1 * n2) % 2) == 0:
        print(f'{n1} * {n2} = {n1 * n2} - even')
    elif ((n1 * n2) % 2) != 0:
        print(f'{n1} * {n2} = {n1 * n2} - odd')
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        dev_res = n1 / n2
        print(f'{n1} / {n2} = {dev_res:.2f} ')
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        dev_res = n1 % n2
        print(f'{n1} % {n2} = {dev_res} ')
