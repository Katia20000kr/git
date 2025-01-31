import csv
import os

file_path = "C:/Users/Katia/Python/users/users.csv"

print("Checking if file exists:", os.path.exists(file_path))

input_username = input("Username: ").strip()
input_pin = input("PIN: ").strip()

user_found = False

try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['username'] == input_username and row['pin'] == input_pin:
                print(f"Welcome {row['fullname']}!")
                user_found = True
                break
        if not user_found:
            print("Sorry, user not found.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except PermissionError:
    print(f"Permission denied for the file '{file_path}'. Please check file permissions.")
