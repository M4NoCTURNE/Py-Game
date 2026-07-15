import random

def play_game():
    # Define the possible moves
    options = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'q' to quit.")

    while True:
        # Get user input and normalize it
        user_choice = input("\nEnter your choice: ").lower()
        
        # Check if the user wants to quit
        if user_choice == 'q':
            print("Thanks for playing! Goodbye.")
            break
        
        # Validate user input
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(options)
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play_game()   
