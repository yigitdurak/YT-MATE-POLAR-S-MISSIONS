import random  # Import the library needed for random number generation

# Generate a random number between 1 and 100

secret_number = random.randint(1, 100)

# Initialize the number of attempts allowed
attempts = 5 

print("I picked a number between 1 and 100. You have 5 attempts!")

# Start the game loop. Runs as long as attempts are greater than 0
while attempts > 0:
    # Ask the user for input and convert it to an integer
    guess = int(input("Enter your guess: "))

    # Check if the guess matches the secret number
    if guess == secret_number:
        print("Congratulations! You guessed right!")
        break # Exit the loop because the user won
    
    # Give hints to help the user
    elif guess < secret_number:
        print("Try a LARGER number.")
    else:
        print("Try a SMALLER number.")

    # Decrease the attempt count after each wrong guess
    attempts = attempts - 1
    print(f"Attempts remaining: {attempts}")

# Check if the user ran out of attempts (Game Over condition)
if attempts == 0:
    print(f"Sorry, you ran out of attempts. The number was: {secret_number}")
