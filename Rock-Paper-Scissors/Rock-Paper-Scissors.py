import random
import datetime

#game
def play_game():
    username = input("Enter your username: ")
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Please type your choice.")

    while user_score < 10 and computer_score < 10:
        choices = ('rock', 'paper', 'scissors')
        user_choice = input("Your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: {username} {user_score} - {computer_score} Computer")

    if user_score == 10:
        print(f"Congratulations {username}, you won the game!")
    else:
        print("Computer won the game. Better luck next time!")

    #score
    with open("scores.txt", "a") as file:
        file.write(f"{username}, {datetime.datetime.now()}, {user_score}, {computer_score}\n")

    update_top5(username, user_score)

#top 5 players 
def update_top5(username, user_score):
    try:
        with open("top5.txt", "r") as file:
            scores = []
            for line in file:
                name, score = line.strip().split(", ")
                scores.append((name, int(score)))
    except FileNotFoundError:
        scores = []

    scores.append((username, user_score))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    with open("top5.txt", "w") as file:
        for name, score in scores:
            file.write(f"{name}, {score}\n")

def display_top_players():
    try:
        with open("top5.txt", "r") as file:
            print("Top 5 Players:")
            for i, line in enumerate(file, 1):
                name, score = line.strip().split(", ")
                print(f"{i}. {name} - Score: {score}")
    except FileNotFoundError:
        print("No top 5 players recorded yet.")

# menu
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Play Game")
        print("2. Show Top 5 Players")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            display_top_players()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

