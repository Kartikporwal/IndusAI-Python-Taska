import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the game
guess_the_number()
