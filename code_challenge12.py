for j in range(0, 6):
    for o in range(6, j, -1):
        print(" ", end=" ")
    for k in range(1, j+1):
        print("*", end=" ")
    for e in range(0, j+1):
        print("*", end=" ")
    print()

for e in range(0, 7):
    for y in range(0, 5):
        print(" ", end=" ")
    for t in range(0, 3):
        print("*", end=" ")
    print()