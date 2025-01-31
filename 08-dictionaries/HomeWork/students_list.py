
students = ['John Doe', 'Mary Smith', 'Andrew Green', 'Lisa Tomas', 'Mike Smith', 'Alex Green']

username_counts = {}

usernames = []

# Process each student in the list
for student in students:
    first_name, last_name = student.split()
    
    username = f"{first_name[0].lower()}{last_name.lower()}"
    
    # Check if the username already exists
    if username in username_counts:
        username_counts[username] += 1
        unique_username = f"{username}{username_counts[username]}"
    else:
        # Initialize the counter for this username
        username_counts[username] = 0
        unique_username = username
    
    usernames.append(unique_username)

print("Generated usernames:", usernames)
