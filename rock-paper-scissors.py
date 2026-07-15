import random

def play_best_of_three():
    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    
    print("--- Best of Three Mode ---")
    print("First to 2 wins takes the match!")

    # 1. Loop runs until someone reaches 2 wins
    while user_wins < 2 and computer_wins < 2:
        user_choice = input("\nEnter your choice: ").lower()
        
        # Validation (removed 'q' check for strict best-of-3)
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue
        
        computer_choice = random.choice(options)
        print(f"You: {user_choice} | Computer: {computer_choice}")
        
        # Determine Round Winner
        if user_choice == computer_choice:
            print("Tie! No points awarded.")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1
            
        # Show current series score
        print(f"Series Score -> You: {user_wins} | Computer: {computer_wins}")

    # 2. Announce Series Winner (Runs automatically after loop ends)
    print("\n--- Match Over ---")
    if user_wins > computer_wins:
        print("Congratulations! You won the best-of-three series!")
    else:
        print("Computer wins the best-of-three series. Better luck next time!")

if __name__ == "__main__":
    play_best_of_three()   
