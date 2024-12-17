cont = True
count = 0
while cont:
    name = input("Please enter a name: ")

    if name.lower() == "stop":
        print("Loop has now stopped")
        print(f"You have entered {count} names")
        break
        cont = False
    else:
        count += 1 #increment by 1
        continue