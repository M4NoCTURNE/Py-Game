from inputimeout import inputimeout, TimeoutOccurred
import random

def play_game_with_timer():
    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    round_timeout = 5  # Seconds allowed per round

    print(f"Welcome! You have {round_timeout} seconds per round.")

    while user_wins < 2 and computer_wins < 2:
        try:
            # Replace input() with inputimeout()
            user_choice = inputimeout(prompt="\nEnter your choice: ", timeout=round_timeout).lower()
        except TimeoutOccurred:
            print(f"\nTime's up! You took more than {round_timeout} seconds.")
            computer_wins += 1
            print(f"Score -> You: {user_wins} | Computer: {computer_wins}")
            continue

        if user_choice not in options:
            print("Invalid choice.")
            continue

        computer_choice = random.choice(options)
        print(f"You: {user_choice} | Computer: {computer_choice}")

        if user_choice == computer_choice:
            print("Tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win round!")
            user_wins += 1
        else:
            print("Computer wins round!")
            computer_wins += 1

        print(f"Score -> You: {user_wins} | Computer: {computer_wins}")

    print("\n--- Game Over ---")
    if user_wins > computer_wins:
        print("You won the match!")
    else:
        print("Computer won the match!")

if __name__ == "__main__":
    play_game_with_timer()    
