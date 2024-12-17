#factorial
name = input("NAME: ")
num = eval(input("Enter a Number: "))
factorial = 1

for b in range(num, 0, -1):
    factorial *= b
print(f"The factorial of {num} is {factorial}")

print("Congratulations " + name)