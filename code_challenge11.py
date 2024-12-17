for j in range(0, 5):
    for o in range(5, j, -1):
        print(" ", end=" ")
    for k in range(1, j+1):
        print("*", end=" ")
    for e in range(0, j+1):
        print("*", end=" ")
    print()

for m in range(1, 5):
    for t in range(0, m+1):
        print(" ",end=" ")
    for q in range(4, m, -1):
        print("*",end=" ")
    for d in range(5, m, -1):
        print("*",end=" ")
    print()