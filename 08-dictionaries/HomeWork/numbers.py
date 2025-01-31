
# Ask the user for 3 numbers
a = int(input("Enter the starting point (a): "))
b = int(input("Enter the ending point (b): "))
c = int(input("Enter the step (c): "))

# Check if we need to step up or step down
if a < b:
    for i in range(a, b + 1, c):
        print(i, end=", ")
else:
    for i in range(a, b - 1, -c):
        print(i, end=", ")
