
import random

lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Combine all lists for easy selection
all_characters = [lower_case_letters, upper_case_letters, digits, special_characters]

def generate_password(length=10):
    password = [
        random.choice(lower_case_letters),
        random.choice(upper_case_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password with random characters from all categories
    while len(password) < length:
        chosen_list = random.choice(all_characters)
        password.append(random.choice(chosen_list))
    
    random.shuffle(password)
    
    return "".join(password)

print("Generated password:", generate_password())
