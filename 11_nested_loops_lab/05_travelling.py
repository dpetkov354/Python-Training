# 5 Travelling
trip_end = False

while not trip_end:
    destination = input()
    if destination == "End":
        trip_end = True
        break
    input_min_cost = input()
    if input_min_cost == "End":
        trip_end = True
        break
    else:
        min_cost = float(input_min_cost)
        while min_cost > 0:
            deposit = float(input())
            min_cost -= deposit
        print(f"Going to {destination}!")
