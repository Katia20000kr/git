import string

# Ask the user for a word
word_to_find = input("Enter a word to search in the story: ").strip().lower()

# Initialize the counter
word_count = 0

# Open the story.txt file and process it
try:
    with open("story.txt", "r") as file:
        # Read all lines in the file
        for line in file:
            # Remove punctuation from the line
            clean_line = line.translate(str.maketrans("", "", string.punctuation))
            # Convert the line to lowercase and split it into words
            words = clean_line.strip().lower().split()
            # Count occurrences of the word in the current line
            word_count += words.count(word_to_find)
except FileNotFoundError:
    print("The file 'story.txt' was not found.")
else:
    print(f"The word '{word_to_find}' appears {word_count} times in the story.")
import os
print("Current working directory:", os.getcwd())
