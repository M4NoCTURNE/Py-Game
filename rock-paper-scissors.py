import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    # 1. Initialize Score Variables
    user_wins = 0
    computer_wins = 0
    ties = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'q' to quit.")

    while True:
        user_choice = input("\nEnter your choice: ").lower()
        
        if user_choice == 'q':
            print("\n--- Final Results ---")
            print(f"You won: {user_wins} times")
            print(f"Computer won: {computer_wins} times")
            print(f"Ties: {ties}")
            
            # Optional: Calculate win percentage
            total_games = user_wins + computer_wins + ties
            if total_games > 0:
                win_percentage = (user_wins / total_games) * 100
                print(f"Win Percentage: {win_percentage:.2f}%")
            
            print("Thanks for playing! Goodbye.")
            break
        
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(options)
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # 2. Determine Winner and Update Scores
        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1  # Increment tie counter
            
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
            user_wins += 1  # Increment user counter
            
        else:
            print("You lose!")
            computer_wins += 1  # Increment computer counter
        
        # 3. Display Current Scoreboard
        print(f"Score -> You: {user_wins} | Computer: {computer_wins} | Ties: {ties}")

if __name__ == "__main__":
    play_game()   
