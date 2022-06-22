# 1 Numbers from 1 to 100
for number in range(1, 101):
    print(number)

# 2 Numbers 1...N with Step 3
n = int(input())
for i in range(1, n + 1, 3):
    print(i)

# 3 Even Powers of 2
n = int(input())
num = 1
for i in range(0, n + 1, 2):
    print(num)
    num = num * 2 * 2

# 4 Numbers N...1
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 5 Character Sequence
inp_text = input()

for i in inp_text:
    print(i)

# 6 Vowels Sum
inp_text = input()
total = 0

for i in range(0, len(inp_text)):
    if inp_text[i] == "a":
        total += 1
    if inp_text[i] == "e":
        total += 2
    if inp_text[i] == "i":
        total += 3
    if inp_text[i] == "o":
        total += 4
    if inp_text[i] == "u":
        total += 5
print(total)

# 7 Sum Numbers
text = int(input())
tot = []

for i in range(0, text):
    tot.append(int(input()))
print(f'{sum(tot)}')

# 8 Number sequence
import sys
smallest = sys.maxsize
biggest = -sys.maxsize
n = int(input())
for i in range(0, n):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")

# 9 Left and Right Sum
n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    left_sum = left_sum + int(input())
for i in range(1, n + 1):
    right_sum = right_sum + int(input())
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")

# 10 Odd Even Sum
n = int(input())
odd_sum = 0
even_sum = 0
for i in range(1, n + 1):
    element = int(input())
    if i % 2 == 0:
        even_sum += element
    else:
        odd_sum += element

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {diff}")
