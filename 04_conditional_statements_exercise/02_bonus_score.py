# 2 Bonus Score
points = int(input("Enter bonus points:"))
bonus = 0

if points <= 100:
    bonus = bonus + 5
elif points > 1000:
    bonus = points * 0.1
else:
    bonus = points * 0.2

if points % 2 == 0:
    bonus = bonus + 1
elif points % 5 == 0:
    bonus = bonus + 2

print(f'Total bonus is:', bonus)
print(f'Total points plus bonus is:', (bonus + points))
