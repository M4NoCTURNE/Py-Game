# 🎮 Rock, Paper, Scissors: Advanced Edition

A fast-paced, console-based **Rock, Paper, Scissors** game built in Python, featuring competitive match modes and time-attack mechanics.

## 🚀 Key Features

### ⏱️ Round Timer
Adds pressure to every decision with a configurable countdown per round.
*   **Mechanism**: Uses the `inputimeout` library to interrupt input after a set duration.
*   **Default Setting**: 5 seconds per move.
*   **Timeout Penalty**: If the timer expires, the round is automatically forfeited to the computer.
*   **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.

### 🏆 Best-of-Three Match Mode
Transforms the game from single rounds into a structured match series.
*   **Win Condition**: The first player to reach **2 wins** claims the match.
*   **Dynamic Length**: Matches can end in 2 rounds (2-0 sweep) or go to a decisive 3rd round (1-1 tie).
*   **Tie Handling**: Tied rounds do not award points, ensuring a clear winner is decided by actual victories.
*   **Auto-End**: The game loop terminates immediately once a player reaches the majority score.

### 📊 Live Score Tracking
Real-time statistics keep players informed throughout the session.
*   **Round-by-Round Updates**: Displays current wins for both User and Computer after every move.
*   **Match Summary**: Upon completion, prints a final report including total wins, losses, ties, and win percentage.

## 🛠️ Technical Requirements

*   **Language**: Python 3.x
*   **External Dependency**: `inputimeout` (Required for the timer feature)
    *   Install via terminal: `pip install inputimeout`

## 🎯 How to Play

1.  **Launch**: Run the script (`python game.py`).
2.  **Input**: Type `rock`, `paper`, or `scissors` within the time limit.
3.  **Compete**: Win 2 rounds before the computer does to win the match.
4.  **React**: Watch the live scoreboard update after every round.  
