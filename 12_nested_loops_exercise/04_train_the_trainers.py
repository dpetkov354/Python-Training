# 4 Train The Trainers
number_of_jury = int(input())
total_avg = 0
score_count = 0
finish = False

while not finish:
    name_of_presentation = input()
    current_avg = 0
    if name_of_presentation == 'Finish':
        finish = True
        break
    for i in range(0, number_of_jury):
        score_per_jury = float(input())
        score_count += 1
        current_avg += score_per_jury
    total_avg += current_avg
    print(f"{name_of_presentation} - {(current_avg / number_of_jury):.2f}.")
print(f"Student\'s final assessment is {(total_avg / score_count):.2f}.")
