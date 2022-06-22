# 7 Trekking Mania
trekker_groups = int(input())
sum_trekkers = 0
musala_num = 0
montblanc_num = 0
kilimandjaro_num = 0
k2_num = 0
everest_num = 0

for i in range(0, trekker_groups):
    num_of_trekkers = int(input())
    sum_trekkers += num_of_trekkers
    if num_of_trekkers <= 5:
        musala_num += num_of_trekkers
    elif 6 <= num_of_trekkers <= 12:
        montblanc_num += num_of_trekkers
    elif 13 <= num_of_trekkers <= 25:
        kilimandjaro_num += num_of_trekkers
    elif 26 <= num_of_trekkers <= 40:
        k2_num += num_of_trekkers
    elif 41 <= num_of_trekkers:
        everest_num += num_of_trekkers
print(f'{((musala_num / sum_trekkers) * 100):.2f}%')
print(f'{((montblanc_num / sum_trekkers) * 100):.2f}%')
print(f'{((kilimandjaro_num / sum_trekkers) * 100):.2f}%')
print(f'{((k2_num / sum_trekkers) * 100):.2f}%')
print(f'{((everest_num / sum_trekkers) * 100):.2f}%')
