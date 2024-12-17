triangle = eval(input("How many tables do you want?: "))

for h in range(1, 11):
    for k in range(1, triangle + 1):
        print(f"{h * k}", end="\t")
    print()