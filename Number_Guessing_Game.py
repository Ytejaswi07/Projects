import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess(1 to 100): "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def provide_feedback(guess, number):
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")

def play_game():
    number = generate_random_number()
    attempts = 0
    
    while True:
        guess = get_user_guess()
        attempts += 1
        provide_feedback(guess, number)
        
        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
