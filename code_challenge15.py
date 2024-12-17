# Hybrid Loop

cont = True
ha = 0

while cont:
    que = input("Do you still want to make new triangles? (yes or no) --> ")

    if que.lower() == "no":
        print("Program Terminated")
        break

    elif que.lower() == "yes":
        ha += 1
        for j in range(1, 6):
            for k in range(1, ha + 1):
                for o in range(1, j+1):
                    print(o, end=" ")
                for t in range(6, j, -1):
                    print(" ", end=" ")
            print()
        continue
    else:
        print("Invalid answer, please specify your answer if it is 'yes' or 'no'")
        continue