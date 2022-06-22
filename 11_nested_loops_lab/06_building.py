# 6 Building
floors = int(input())
living_space = int(input())
for i in range(floors, 0, -1):
    for n in range(0, living_space):
        if i == floors:
            print("L{0}{1}".format(i, n), end=" ")
        elif i % 2 == 0:
            print("O{0}{1}".format(i, n), end=" ")
        else:
            print("A{0}{1}".format(i, n), end=" ")
    print("")
