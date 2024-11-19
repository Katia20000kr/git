
total = 0
count = 0

while True:
    grade = float(input("Grade: "))
    total += grade
    count += 1
    more = input("Continue? (yes/no): ").lower()
    if more != "yes":
        break

average = total / count
print(f"AVERAGE: {average}")
