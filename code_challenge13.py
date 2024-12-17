for u in range(1, 6):
    for n in range(6, u, -1):
        print(" ", end=" ")
    for a in range(u, 1, -1):
        print(a, end=" ")
    for k in range(1, u+1):
        print(k, end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(6 - i):
        print(" ", end=" ")
    for p in range(i, 0, -1):
        print(p, end=" ")
    for h in range(2, i + 1):
        print(h, end=" ")
    print()