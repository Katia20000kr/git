
import random

# Step 1: Create a list of random numbers
numbers = [random.randint(1, 100) for _ in range(20)]
print("The list is:", numbers)

# Step 2: Find even numbers in the list
even_numbers = [num for num in numbers if num % 2 == 0]

# Step 3: Print the even numbers
print("The even numbers are:", even_numbers)
