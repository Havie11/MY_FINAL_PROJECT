for j in range(1, 6):
    for u in range(6, j, -1):
        print(" ", end=" ")
    for k in range(1, j+1):
        print("*", end=" ")
    for e in range(1, j+1):
        print("*", end=" ")
    print()

for m in range(1, 6):
    for a in range(1, m+1):
        print(" ",end=" ")
    for n in range(6, m, -1):
        print("*",end=" ")
    for h in range(6, m, -1):
        print("*",end=" ")
    print()