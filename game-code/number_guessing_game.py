import random

# Welcome message
def welcome_message():
    print("🎉 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it within the limited number of attempts!\n")

# Function to allow the user to select difficulty level
def choose_difficulty():
    print("Choose difficulty:")
    print("1 - Easy (10 tries)")
    print("2 - Medium (7 tries)")
    print("3 - Hard (5 tries)")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 10 
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Main function that runs the guessing game
def play_game():
    welcome_message()
    max_attempts = choose_difficulty()  # Get the number of allowed attempts
    secret_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # To track the number of guesses

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1} of {max_attempts}. Enter your guess: "))
            
            # Check if the guess is within the valid range
            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            attempts += 1  # Increment attempts after a valid input

            # Check if the guess is correct
            if guess == secret_number:
                print(f"🎊 Congratulations! You guessed it right in {attempts} tries!")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
        except ValueError:
            print("❌ Please enter a valid number.")  # Handle non-integer input
    
    else:
        # If user runs out of attempts
        print(f"\n💥 Game Over! The number was: {secret_number}")

# Function to ask the user if they want to play again
def play_again():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again == "yes":
            return True
        elif again == "no":
            print("👋 Thanks for playing! Goodbye!")
            return False
        else:
            print("Please type 'yes' or 'no'.")

# Main loop to keep the game running until the user quits
while True:
    play_game()
    if not play_again():
        break
