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
