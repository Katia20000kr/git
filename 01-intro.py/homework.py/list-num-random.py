
import random

# Create a list with 20 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(20)]

# Count how many of the numbers are even
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

# Print the list and the count of even numbers
print("Numbers:", numbers)
print("Count of even numbers:", even_count)
