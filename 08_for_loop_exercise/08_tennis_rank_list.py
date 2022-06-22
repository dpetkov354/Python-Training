# 8 Tennis Rank list
tournaments = int(input())
initial_points = int(input())
fin_points = initial_points
average_points = 0
win_rate = 0

for i in range(0, tournaments):
    type_of_t = input()
    if type_of_t == "W":
        fin_points += 2000
        average_points += 2000
        win_rate += 1
    elif type_of_t == "F":
        fin_points += 1200
        average_points += 1200
    elif type_of_t == "SF":
        fin_points += 720
        average_points += 720
print(f"Final points: {fin_points}")
print(f"Average points: {int(average_points / tournaments)}")
print(f"{((win_rate / tournaments) * 100):0.2f}%")
