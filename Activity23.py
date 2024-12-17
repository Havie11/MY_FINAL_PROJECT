# Functions and Scopes
#  Basic of Functions - block of code which only runs when it is called.
# Functions

# Creating a function
# def my_function():
#     print("Hello from a function")

# Calling a function
# my_function()

# def fun(fname):
#     print(f"Hi, {fname}, Hope you're having a delightful Monday(I Miss You)")

# fun("Hainsa")


# Function with Return Values

def factorial(number):
    fact = 1
    for n in range(number, 0, -1):
        fact *= n
    return fact

addsomething = 10 + factorial(5)
print(f"The result of the factorial plus 10 is {addsomething}")