
def programenu():

    print("Hi! Welcome to this Program")
    ask = input("\nMENU LISTS \n1. ESCAPE SEQUENCE \n2. ARITHMETIC OPERATORS \n3. ASSIGNMENT OPERATORS \n4. RELATIONAL OPERATORS \n5. LOGICAL OPERATORS \n6. CONDITIONAL STATEMENTS \n7. LOOPING STATEMENTS \n8. FOR LOOP \n9. WHILE LOOP \n10. EXIT \nENTER YOUR CHOICE HERE:  ")
    
    while True:
        if ask == "1":
            print("\n=====================================================================")
            print("\nWELCOME! HERE'S THE ESCAPE SEQUENCE")
            print("\nFirst, we must know what does the Escape Sequence means. \n\nEscape sequences are special character combinations used to represent characters that are \ndifficult or impossible to type directly, such as newline, tab, or backslash itself. \nThey are preceded by a backslash () and followed by a specific character.")
            print("\n=====================================================================")
            break

        elif ask == "2":
            print("\n=====================================================================")
            print("\nWELCOME! HERE'S THE ARITHMETIC OPERATORS")
            print("\nWhat are the Arithmetic Operators? \n\nSo these are symbols used in programming languages to perform mathematical operations. \nThey are essential for calculations and manipulating numerical data. \n\nHere's a breakdown of common arithmetic operators:")
            print("\n=====================================================================")
            que = input("\n1. ADDITION \n2. SUBTRACTION \n3. MULTIPLICATION \n4. DIVISION \n5. MODULUS \n6. EXPONENTIATION \n7. FLOOR DIVISION \nINPUT YOUR CHOICE HERE:  ")
            
            while True:
                if que == "1":
                    print("\n=====================================================================")
                    print("\nADDITION")
                    print("\nThis adds two numbers together. ( + )")
                    print("Example: 5 + 6 = 11")
                    print("\n=====================================================================")
                    print("\nHERE, LET'S PLAY A GAME ABOUT ADDITION...")
                    print("\n=====================================================================")
                    
                    import random
                    def addition_game():
                        """Plays an addition game with the user."""
                        score = 0
                        num_que = 10 #Number of questions to ask
                        print("\n=====================================================================")
                        print("WELCOME TO THE ADDITION GAME!")
                        print("In this game, you will be asked to solve five addition problems.")
                        
                        for _ in range(num_que):
                            num1 = random.randint(1,1000)
                            num2 = random.randint(1,1000)

                            print(f"What is {num1} + {num2}?")

                            answer = input("Enter your answer:  ")

                            try:
                                user_answer = int(answer)
                                correct_answer = num1 + num2

                                if user_answer == correct_answer:
                                    print("CORRECT!")
                                    score += 1
                                else:
                                    print(f"Incorrect. The correct answer is {correct_answer}.")

                            except ValueError:
                                print(f"Invalid Input. Please Enter a Number. ")

                        print(f"\nYou got {score} out of {num_que} questions correct!")
                    print("\n=====================================================================")
                    addition_game()
                    break
                
                elif que == "2":
                    print("\n=====================================================================")
                    print("\nSUBTRACTION")
                    print("\nSubtraction is one of the four basic operations of arithmetic. \nIt is the process of taking away one number from another. \nThe result of subtraction is called the difference.")
                    print("For example, 5 - 3 = 2. Here, 5 is the minuend, 3 is the subtrahend, and 2 is the difference.")
                    print("\n=====================================================================")
                    print("\nHERE! LET'S PLAY SOME GAME!")
                    print("\n=====================================================================")
                    
                    import random

                    def subtraction_game():
                        """ A subtraction game where two players take turns subtracting numbers from a starting value. \nThe player who subtracts the last number wins. """
                        
                        # Get the starting number from the user.
                        startnum = int(input("Enter the Starting Number:  "))

                        # Initialize the current number.
                        currentnum = startnum

                        # Initialize the current player.
                        currentplayer = 1

                        # Game Loop
                        while currentnum > 0:
                            # Display the current number
                            print(f"Current number: {currentnum}")

                            # Get the player's input.
                            while True:
                                try:
                                    sub_value = int(input(f"Player {currentplayer}, enter a number to subtract (1 to {min(currentnum, 9)}):  "))
                                    if 1 <= sub_value <= min(currentnum, 9):
                                        break
                                    else:
                                        print("Invalid Input. Please enter a number between 1 and 9.")
                                except ValueError:
                                    print("Invalid Input. Please enter a number.")
                            # Subtract the number
                            currentnum -= sub_value

                            # Switch to the next player
                            currentplayer = 2 if currentplayer == 1 else 1

                            # Declare the winner
                            print(f"Player {currentplayer} wins!")

                    # Start the Game
                    subtraction_game()
                    print("\n=====================================================================")
                    break
                elif que == "3":
                    print("\n=====================================================================")
                    print("\nMULTIPLICATION")
                    print("Multiplication is one of the four basic operations in arithmetic, \nalongside addition, subtraction, and division. It is the process of repeated addition.")
                    print("For example, 3 x 4 means adding 3 four times: 3 + 3 + 3 + 3 = 12.")
                    print("\n=====================================================================")
                    print("\nCOME ON LET'S PLAY!")
                    print("\n=====================================================================")

                    import random
                    def multiplication_game():
                        """A multiplication game where players try to solve multiplication problems"""

                        # Welcome Message
                        print("Welcome to the Multiplication Game!")

                        # Game Loop
                        while True:
                            # Generate to random numbers.
                            n1 = random.randint(1,12)
                            n2 = random.randint(1,12)

                            # Display the Multiplication Problem
                            print(f"\nWhat is {n1} x {n2}?")

                            # Get the players answer
                            while True:
                                try:
                                    answer = int(input("YOUR ANSWER:  "))
                                    break
                                except ValueError:
                                    print("Invalid Input. Please Enter a Number.")

                            # Check the answer
                            if answer == n1 * n2:
                                print("CORRECT!")
                            else:
                                print(f"Incorrect. The correct answer is {n1 * n2}.")

                            # Ask if the player wants to play again.
                            play_again = input("PLAY AGAIN? (Yes/No):  ")
                            if play_again != 'yes':
                                break
                    print("\n=====================================================================")
                    multiplication_game()
                    break
                elif que == "4":
                    print("\n=====================================================================")
                    print("DIVISION")
                    print("Division is one of the four basic arithmetic operations, \nalongside addition, subtraction, and multiplication. \nIt involves splitting a whole into equal parts.")
                    print("Example: \nIf we divide 15 by 3, we have: \nDividend: 15 \nDivisor: 3 \nQuotient: 5 (because 15 divided by 3 equals 5) \nRemainder: 0 (because 15 is perfectly divisible by 3)")
                    print("\n=====================================================================")
                    print("\nHERE, LET'S PLAY A SIMPLE GAME!")
                    print("\n=====================================================================")

                    import random

                    def division_game():
                        """Plays a division game where the user needs to guess the quotient."""

                        while True:
                            dividend = random.randint(10, 100)
                            divisor = random.randint(2, 10)
                            quotient = dividend // divisor

                            print(f"What is {dividend} divided by {divisor}?")
                            try:
                                user_answer = int(input("Enter your answer: "))
                                if user_answer == quotient:
                                    print("Correct! You're a division master!")
                                    break
                                else:
                                    print(f"Incorrect. The correct answer is {quotient}.")
                            except ValueError:
                                print("Please enter a valid integer.")
                    print("\n=====================================================================")
                    division_game()
                    break
                elif que == "5":
                    print("\n=====================================================================")
                    print("MODULUS")
                    print("The modulus (also known as the modulo operation) is a \nmathematical operation that finds the remainder of a division.")
                    print("A 12-hour clock uses the modulus operation. \nFor example, 14 hours after 12:00 is 2:00. This is because (14 % 12) = 2.")
                    print("\n=====================================================================")
                    print("\nLET'S PLAY SOME GAME!")
                    print("\n=====================================================================")

                    import random

                    def modulus_game():
                        """Plays a modulus game where the user needs to guess the remainder of a division."""

                    print("Welcome to the Modulus Madness Game!")
                    print("Let's see how well you understand remainders!")
                    print("------------------------------------------")

                    while True:
                        # Generate random numbers for the problem
                        dividend = random.randint(10, 100)  # Dividend between 10 and 100
                        divisor = random.randint(2, 10)    # Divisor between 2 and 10

                        # Calculate the correct remainder
                        remainder = dividend % divisor

                        # Print the division problem and ask for the remainder
                        print(f"What is the remainder when {dividend} is divided by {divisor}?")

                        # Get the user's answer
                        try:
                            user_answer = int(input("Enter your answer: "))
                        except ValueError:
                            print("Oops! Please enter a whole number.")
                            continue  # Go back to asking for the answer

                        # Check if the answer is correct
                        if user_answer == remainder:
                            print("That's right! You're a modulus master!")
                            break  # End the game if correct
                        else:
                            print(f"Not quite. The correct remainder is {remainder}.")
                            print("Keep trying!")

                        # Give a little extra explanation for the user
                        print("Remember: The remainder is what's left over after the division.")
                        print(f"For example, 15 divided by 4 gives a quotient of 3 and a remainder of 3.")
                        print("Because 4 goes into 15 three times, with 3 left over.")

                    print("\n=====================================================================")
                    modulus_game()
                    break
                elif que == "6":
                    print("\n=====================================================================")
                    print("EXPONENTIATION")
                    print("Exponentiation is a mathematical operation that involves raising a \nbase number to a certain power, called the exponent. \nIt represents repeated multiplication of the base by itself.")
                    print("Example: \n2<sup>3</sup> = 2 * 2 * 2 = 8 \nHere, 2 is the base and 3 is the exponent. \nThe result of 2 raised to the power of 3 is 8.")
                    print("\n=====================================================================")
                    print("\nCOME ON, LET'S PLAY A GAME")
                    print("\n=====================================================================")

                    import random

                    def exponentiation_game():
                        """ A simple exponentiation game for users to practice their skills. """

                        # Generate random numbers for base and exponent
                        base = random.randint(2, 10)
                        exponent = random.randint(2, 5)

                        # Calculate the correct answer
                        correct_answer = base ** exponent

                        # Prompt the user for their answer
                        print(f"What is {base} raised to the power of {exponent} ({base}^{exponent})?")
                        user_answer = int(input("Enter your answer: "))

                        # Check if the user's answer is correct
                        if user_answer == correct_answer:
                            print("Congratulations! You got it right!")
                        else:
                            print(f"Oops, the correct answer is {correct_answer}.")
                    print("\n=====================================================================")
                    # Start the game
                    exponentiation_game()
                    break
                elif que == "7":
                    print("\n=====================================================================")
                    print("FLOOR DIVISION")
                    print("Floor division in programming is a type of division that always \nrounds the result down to the nearest whole number, discarding any remainder. \nIt's represented by the double slash operator (//) in most programming languages. \nExample: 7 // 3 = 2 (Since 7 divided by 3 is 2.333..., the floor division rounds down to 2)")
                    print("\n=====================================================================")
                    print("\nLET'S PLAY A GAME!")
                    print("\n=====================================================================")

                    import random

                    def floor_division_game():
                        """A floor division game with multiple levels of difficulty."""

                        # Game levels and their corresponding number ranges
                        levels = {
                            "Easy": (1, 10),
                            "Medium": (10, 50),
                            "Hard": (50, 100)
                        }

                        # Choose a difficulty level
                        print("Choose a difficulty level:")
                        for level in levels:
                            print(level)
                        difficulty = input("Enter your choice: ").capitalize()

                        # Validate user input
                        while difficulty not in levels:
                            print("Invalid choice. Please choose from the available levels.")
                            difficulty = input("Enter your choice: ").capitalize()

                        # Get number range for the chosen difficulty
                        min_num, max_num = levels[difficulty]

                        # Generate random numbers for the dividend and divisor
                        dividend = random.randint(min_num, max_num)
                        divisor = random.randint(1, min_num)

                        # Calculate the correct answer
                        correct_answer = dividend // divisor

                        # Prompt the user for their answer
                        print(f"What is the floor division of {dividend} by {divisor} ({dividend} // {divisor})?")
                        user_answer = int(input("Enter your answer: "))

                        # Check if the user's answer is correct
                        if user_answer == correct_answer:
                            print("Congratulations! You got it right!")
                        else:
                            print(f"Oops, the correct answer is {correct_answer}.")

                    # Start the game
                    floor_division_game()
                    print("\n=====================================================================")
                    break
            break
        elif ask == "3":
            print("\n=====================================================================")
            print("\nWELCOME! HERE'S THE ASSIGNMENT OPERATORS")
            print("\nAssignment operations are used to assign values to variables in programming. \nThey are a fundamental part of how you store and manipulate data.")
            print("Here's a breakdown of common assignment operations:")
            print("\n=====================================================================")
            print("\nAugmented Assignment: \nThese operators combine an arithmetic operation with assignment, making code more concise.")
            print("+=   (Add and Assign): Adds the right operand to the left operand and assigns the result to the left operand.")
            print("-=   (Subtract and Assign): Subtracts the right operand from the left operand and assigns the result to the left operand.")
            print("*=   (Multiply and Assign): Multiplies the left operand by the right operand and assigns the result to the left operand.")
            print("/=   (Divide and Assign): Divides the left operand by the right operand and assigns the result to the left operand.")
            print("%=   (Modulo and Assign): Calculates the remainder of the division of the left operand by the right operand and assigns the result to the left operand.")
            print("**=  (Exponent and Assign): Raises the left operand to the power of the right operand and assigns the result to the left operand.")
            print("//=  (Floor Division and Assign): Performs floor division of the left operand by the right operand and assigns the result to the left operand.)")
            print("\n=====================================================================")

            import random
            import time

            def play_assignment_game():
                """ This function implements a long long game about assignment operations. \nThe player has to guess the value of a variable after a series of operations. """

                print("Welcome to the Assignment Operator Challenge!")
                print("You'll be given a variable and a series of operations.")
                print("Your goal is to guess the final value of the variable after each operation.")
                print("Good luck!")

                # Game loop
                while True:
                    # Initialize variables
                    variable_name = "x"
                    variable_value = random.randint(1, 100)
                    operations = []
                    num_operations = random.randint(3, 7)

                    # Generate random operations
                    for _ in range(num_operations):
                        operation = random.choice(["+", "-", "*", "//", "%"])
                        operand = random.randint(1, 20)
                        operations.append((operation, operand))

                    # Print the initial value and operations
                    print(f"\nVariable: {variable_name} = {variable_value}")
                    print("Operations:")
                    for i, (op, val) in enumerate(operations):
                        print(f"{i+1}. {variable_name} {op}= {val}")

                    # Apply operations and track the value
                    for op, val in operations:
                        if op == "+":
                            variable_value += val
                        elif op == "-":
                            variable_value -= val
                        elif op == "*":
                            variable_value *= val
                        elif op == "//":
                            variable_value //= val
                        elif op == "%":
                            variable_value %= val

                    # Get player's guess
                    guess = int(input(f"\nGuess the final value of {variable_name}: "))

                    # Check the answer
                    if guess == variable_value:
                        print("Correct! You're a master of assignment operations!")
                    else:
                        print(f"Incorrect. The final value of {variable_name} was {variable_value}.")

                    # Ask if the player wants to play again
                    play_again = input("Do you want to play again? (y/n): ").lower()
                    if play_again != 'y':
                        break
            print("\n=====================================================================")
            play_assignment_game()
            break
        elif ask == "4":
            print("\n=====================================================================")
            print("WELCOME! HERE'S THE RELATIONAL OPERATORS")
            print("Relational operators are used to compare values in programming. \nThey help you determine the relationship between two operands, \nresulting in a boolean value (either True or False).")
            print("Here's a breakdown of common relational operators:")
            print("Operator	        Meaning                 Example	    Result")
            print("   ==	    Equal to	                5 == 5	    True")
            print("   !=	    Not equal to	            5 != 10	    True")
            print("   >	        Greater than	            10 > 5	    True")
            print("   <	        Less than	                5 < 10	    True")
            print("   >=	    Greater than or equal to	10 >= 10	True")
            print("   <=	    Less than or equal to	    5 <= 10	    True")
            print("\n=====================================================================")
            print("\nCOME ON, LET'S PLAY A GAME!")
            print("\n=====================================================================")

            import random
            import time

            def play_relational_game():
                """ This function implements a long long game about relational operations. \nThe player has to guess the outcome of a comparison between two numbers, \nusing relational operators. """

                print("Welcome to the Relational Operator Challenge!")
                print("You'll be given two numbers and a relational operator.")
                print("Your goal is to guess if the comparison is True or False.")
                print("Good luck!")

                # Game loop
                while True:
                    # Generate random numbers and operator
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                    operator = random.choice(["==", "!=", ">", "<", ">=", "<="])

                    # Print the comparison
                    print(f"\nNumber 1: {num1}")
                    print(f"Number 2: {num2}")
                    print(f"Operator: {operator}")
                    print(f"Is {num1} {operator} {num2} True or False?")

                    # Get player's guess
                    guess = input("Enter your guess (True/False): ").lower()

                    # Check the answer
                    if eval(f"{num1} {operator} {num2}") == (guess == "true"):
                        print("Correct! You're a relational operator wizard!")
                    else:
                        print(f"Incorrect. The correct answer is {eval(f'{num1} {operator} {num2}')}.")

                    # Ask if the player wants to play again
                    play_again = input("Do you want to play again? (y/n): ").lower()
                    if play_again != 'y':
                        break
            print("\n=====================================================================")
            play_relational_game()
            break
        elif ask == "5":
            print("\n============================================================================================================")
            print("WELCOME! HERE'S THE LOGICAL OPERATORS")
            print("Logical operators are used to combine or manipulate boolean expressions (expressions that evaluate to either True or False). \nThey allow you to create more complex conditions based on the truth values of simpler expressions.")
            print("Here's a breakdown of common logical operators:")
            print("\n============================================================================================================")
            print("Operator	                    Meaning                                Example	            Result")
            print("\n============================================================================================================")
            print("  and	    Logical AND: Returns True if both operands are True;      (5 > 2) and (10 < 20)	    True")
            print("                         otherwise, it returns False.")
            print("\n============================================================================================================")
            print("   or	    Logical OR: Returns True if at least one operand is       (5 > 10) or (10 < 20)	    True")
            print("           True; it returns False only if both operands are False.")
            print("\n============================================================================================================")
            print("  not	    Logical NOT: Inverts the truth value of its operand.           not (5 > 10)	            True")
            print("           If the operand is True, it returns False; if the operand")
            print("                         is False, it returns True.")
            print("\n============================================================================================================")
            print("\n\n=====================================================================")
            print("\nHERE I HAVE SOME GAME FOR YOU!")
            print("\n=====================================================================")
            import random
            import time

            def generate_logical_expression():
                """Generates a random logical expression with two operands and an operator."""
                operands = [random.randint(1, 100) > 50, random.randint(1, 100) < 75]  # Boolean operands
                operator = random.choice(["and", "or"])
                return f"{operands[0]} {operator} {operands[1]}"

            def play_logical_game():
                """Main function for the logical operations game."""
                print("Welcome to the Logical Operator Challenge!")
                print("You'll be given a logical expression. Your goal is to determine if it's True or False.")

                score = 0
                num_rounds = 5  # You can adjust the number of rounds

                for round_num in range(1, num_rounds + 1):
                    print(f"\nRound {round_num}:")
                    expression = generate_logical_expression()
                    print(f"Expression: {expression}")

                    while True:
                        try:
                            answer = input("Is the expression True or False? (True/False): ").lower()
                            if answer in ["true", "false"]:
                                break
                            else:
                                print("Invalid input. Please enter 'True' or 'False'.")
                        except ValueError:
                            print("Invalid input. Please enter 'True' or 'False'.")

                    correct_answer = str(eval(expression)).lower()
                    if answer == correct_answer:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Incorrect. The correct answer was {correct_answer}.")

                    time.sleep(1)  # Pause for a moment

                print(f"\nGame Over! Your final score is {score}/{num_rounds}")
                if score >= num_rounds // 3:
                    print("Congratulations! You're a logical operator master!")
                else:
                    print("Keep practicing your logical skills!")
            print("\n=====================================================================")
            play_logical_game()
            break
        elif ask == "6":
            print("\n=====================================================================")
            print("WELCOME! HERE'S THE CONDITIONAL STATEMENTS")
            print("Conditional statements, also known as control flow statements, \nallow you to execute different blocks of code based on whether a condition is true or false. \nThey are fundamental to creating programs that can make decisions \nand respond dynamically to different situations.")
            print("Here's a breakdown of the main types of conditional statements in most programming languages (illustrated with Python):")
            print("\n=====================================================================")
            print("\n1. if statement")
            print("The simplest form executes a block of code only if a condition is true.")
            print("\n=====================================================================")
            print("\n2. if-else statement")
            print("This allows you to execute one block of code if the condition is true and a different block if it's false.")
            print("\n=====================================================================")
            print("\n3. if-elif-else statement")
            print("This handles multiple conditions sequentially. \nThe first condition that evaluates to true will have its associated block executed; the rest are skipped. \nThe else block (optional) is executed only if none of the preceding conditions are true.")
            print("\n=====================================================================")

            def demonstrate_conditionals():
                """Demonstrates various types of conditional statements."""

                age = int(input("Enter your age: "))
                has_license = input("Do you have a driver's license? (yes/no): ").lower() == "yes"

                print("\n--- Conditional Statements ---")

                # Simple if-else
                if age >= 18:
                    print("You are an adult.")
                else:
                    print("You are a minor.")

                # if-elif-else
                if age >= 65:
                    print("You are a senior citizen.")
                elif age >= 18:
                    print("You are an adult.")
                else:
                    print("You are a minor.")

                # Nested conditionals
                if age >= 16:
                    if has_license:
                        print("You can drive.")
                    else:
                        print("You are old enough to get a driver's license.")
                else:
                    print("You are too young to drive.")

                # Boolean logic (and, or, not)
                is_eligible = age >= 18 and has_license  # Must be 18 or older AND have a license
                if is_eligible:
                    print("You are eligible to rent a car.")
                else:
                    print("You are not eligible to rent a car.")

                is_eligible_vote = age >= 18 or age < 18 and not has_license # You can vote if you're 18 or older.
                if is_eligible_vote:
                    print("You are eligible to vote.")
                else:
                    print("You are too young to vote.")

                #Example with multiple conditions and data types
                temperature = 25
                weather = "sunny"

                if temperature > 30 and weather == "sunny":
                    print("It's a scorching hot sunny day!")
                elif temperature > 20 and weather == "sunny":
                    print("It's a pleasant sunny day.")
                elif temperature > 20 and weather == "cloudy":
                    print("It's a pleasant cloudy day.")
                else:
                    print("The weather is not so good.")

            print("\n=====================================================================")
            # Run the demonstration
            demonstrate_conditionals()
            break
        elif ask == "7":
            print("\n=====================================================================")
            print("WELCOME! HERE'S THE LOOPING STATEMENTS")
            print("Looping statements are a fundamental part of programming, \nallowing you to repeat a block of code multiple times. \nPython offers two main types of loops: for loops and while loops.")
            print("\n=====================================================================")
            print("\nHERE'S A GAME FOR YOU!")
            print("\n=====================================================================")

            import random

            def number_guessing_game():
                """Plays a number guessing game with the user."""

                secret_number = random.randint(1, 100)  # Generates a random number between 1 and 100
                guesses_left = 7
                print("Welcome to the Number Guessing Game!")
                print("I'm thinking of a number between 1 and 100.")

                while guesses_left > 0:
                    print(f"\nYou have {guesses_left} guesses left.")
                    try:
                        guess = int(input("Take a guess: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue  # Skips to the next iteration of the loop

                    if guess < secret_number:
                        print("Too low!")
                    elif guess > secret_number:
                        print("Too high!")
                    else:
                        print(f"Congratulations! You guessed the number {secret_number} in {7 - guesses_left} tries!")
                        return  # Exits the function

                    guesses_left -= 1

                print(f"\nYou ran out of guesses. The number was {secret_number}.")
            
            number_guessing_game()
            break
        elif ask == "8":
            print("\n=====================================================================")
            print("\nWELCOME! HERE'S THE FOR LOOP")
            print("The for loop is a fundamental control flow statement in many programming languages, including Python. \nIt's used to iterate over a sequence (like a list, tuple, string, or range) or other iterable object, \nexecuting a block of code for each item in the sequence.")
            print("The general structure of a for loop is: \nfor item in sequence: \n# Code to be executed for each item")
            print("\n=====================================================================")
            print("item: A variable that takes on the value of each element in the sequence during each")
            print("      iteration. You choose the name item; it doesn't have to be 'item'.")
            print("\n=====================================================================")
            print("sequence: An iterable object (like a list, tuple, string, range, etc.) that provides \nthe values for the loop to process.")
            print("\n=====================================================================")
            print("# Code to be executed...: The indented block of code that will be executed repeatedly \nfor each item in the sequence.")
            print("\n=====================================================================")
            print("\nHERE'S A FUN GAME FOR YOU!")
            print("\n=====================================================================")
            
            # Example 1: Getting the number of greetings from the user

            num_greetings = int(input("How many times do you want to say hello? "))
            print("\nExample 1: Personalized Greetings")
            for i in range(num_greetings):
                print("Hello!")


            # Example 2: Getting a list of items from the user

            num_items = int(input("\nHow many items do you want to list? "))
            items = []
            print("Example 2: Listing Items")
            for i in range(num_items):
                item = input(f"Enter item {i+1}: ")
                items.append(item)

            print("Your list:", items)


            # Example 3: Calculating the sum of numbers provided by the user

            num_numbers = int(input("\nHow many numbers do you want to add? "))
            total = 0
            print("Example 3: Summing Numbers")
            for i in range(num_numbers):
                while True:
                    try:
                        number = float(input(f"Enter number {i+1}: "))
                        total += number
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            print(f"The sum is: {total}")


            # Example 4:  A simple guessing game using a for loop and user input
            import random

            secret_number = random.randint(1,100)
            guesses_left = 7
            print("\nExample 4: Number Guessing Game")
            print("I'm thinking of a number between 1 and 100.")

            for i in range(guesses_left):
                while True:
                    try:
                        guess = int(input(f"You have {guesses_left - i} guesses left.  What's your guess? "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if guess < secret_number:
                    print("Too low!")
                elif guess > secret_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} in {i+1} tries.")
                    break

            if guess != secret_number:
                print(f"You ran out of guesses. The number was {secret_number}.")

            print("\n=====================================================================")
            break

        elif ask == "9":
            print("\n=====================================================================")
            print("\nWELCOME! HERE'S THE WHILE LOOP")
            print("A while loop in programming is a control flow statement that repeatedly \nexecutes a block of code as long as a certain condition remains true. \nIt's like saying, 'Keep doing this until something changes.'")
            print("\n=====================================================================")
            print("\nHERE'S A FUN GAME TO PLAY!")
            print("\n=====================================================================")

            import random
            import time

            def reaction_time_game():
                print("Get ready...")
                time.sleep(random.uniform(2, 5))  # Wait a random time between 2 and 5 seconds
                start_time = time.time()
                input("Press Enter!")
                end_time = time.time()
                reaction_time = end_time - start_time
                print(f"Your reaction time was: {reaction_time} seconds")

            reaction_time_game()
            print("\n=====================================================================")
            break
        elif ask == "10":
            print("\n=====================================================================")
            print("\nTHANK YOU FOR USING THE PROGRAM!")
            print("\n=====================================================================")
            break
        else:
            print("\n=====================================================================")
            print("\nINVALID INPUT!")
            print("\n=====================================================================")
            break
    
programenu()
