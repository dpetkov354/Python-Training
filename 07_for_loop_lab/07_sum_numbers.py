# 7 Sum Numbers
text = int(input())
tot = []

for i in range(0, text):
    tot.append(int(input()))
print(f'{sum(tot)}')
