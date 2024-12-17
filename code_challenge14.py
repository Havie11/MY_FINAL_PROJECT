akkeb = True
hm = 0
total = 0

while akkeb:
    num = eval(input("Enter a number: "))

    if num == 0:
        print("Loop Terminated")
        print(f"You've entered {hm} numbers")
        print(f"The total summation of all the numbers given is: {total}")

    hm += 1
    total += num
    continue