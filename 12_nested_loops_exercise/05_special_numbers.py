# 5 Special Numbers
number = int(input())

for n in range(1111, 9999 + 1):
    n = str(n)
    if n[0] != "0" and n[1] != "0" and n[2] != "0" and n[3] != "0":
        if number % int(n[0]) == 0 and number % int(n[1]) == 0 and number % int(n[2]) == 0 and number % int(n[3]) == 0:
            print(n, end=" ")
