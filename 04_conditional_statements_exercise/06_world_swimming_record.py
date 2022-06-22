# 6 World Swimming Record
import math

record_current = float(input())
distance_to_swim = float(input())
time_1meter = float(input())

swim_time = distance_to_swim * time_1meter
delay_swim_time = math.floor(distance_to_swim / 15) * 12.5
tot_swim_time = round((swim_time + delay_swim_time), 2)

if tot_swim_time < record_current:
    print(f'Yes, he succeeded! The new world record is %.2f seconds.' % tot_swim_time)
elif tot_swim_time >= record_current:
    print(f'No, he failed! He was %.2f seconds slower.' % (tot_swim_time - record_current))
