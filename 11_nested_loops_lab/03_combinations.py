# 3 Combinations
needed_result = int(input())
count = 0

for x1 in range(needed_result + 1):
    for x2 in range(needed_result + 1):
        for x3 in range(needed_result + 1):
            if (x1 + x2 + x3) == needed_result:
                count += 1
print(count)
