import os
import random

def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    return users

def register_user(users):
    while True:
        username = input("Enter a new username: ")
        if username in users:
            print("Username already exists. Try again.")
        else:
            break
    password = input("Enter a password: ")
    users[username] = password
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")
    return username

def login(users):
    for _ in range(3):
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            return username
        print("Incorrect credentials, try again.")
    print("Login failed. Exiting...")
    return None

def load_questions():
    file_path = "questions.txt"
    questions = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    question, correct, wrong1, wrong2, wrong3 = parts
                    questions.append((question, correct, [correct, wrong1, wrong2, wrong3]))
    return questions

def play_quiz():
    questions = load_questions()
    if not questions:
        print("No questions found!")
        return 0
    
    score = 0
    random.shuffle(questions)
    selected_questions = random.sample(questions, min(5, len(questions)))

    for i, (question, correct, options) in enumerate(selected_questions):
        print(f"{i+1}. {question}")
        random.shuffle(options)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        answer = input("Select the correct answer (1-4): ")
        if options[int(answer) - 1] == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct}")

    print(f"Final Score: {score}/5")
    return score

def update_scores(username, score):
    with open("scores.txt", "a") as file:
        file.write(f"{username},{score}\n")

def main():
    users = load_users()
    choice = input("Do you have an account? (yes/no): ").lower()

    if choice == "no":
        username = register_user(users)
    else:
        username = login(users)
        if not username:
            return

    while True:
        score = play_quiz()
        update_scores(username, score)
        again = input("Do you want to play again? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
