import string
import os


file_path = "C:/Users/Katia/Python/home/story.txt"


print("Checking if file exists:", os.path.exists(file_path))


word_to_find = input("Enter a word to search in the story: ").strip().lower()


word_count = 0


try:
    with open(file_path, "r") as file:
        for line in file:
            
            clean_line = line.translate(str.maketrans("", "", string.punctuation))
            
            words = clean_line.strip().lower().split()
            
            word_count += words.count(word_to_find)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
else:
    print(f"The word '{word_to_find}' appears {word_count} times in the story.")

