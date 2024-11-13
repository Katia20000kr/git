total_score = 0
count = 0

while True:
    score = int(input("Enter a score (or type '-1' to stop): "))
    if score == -1:
        break
    
    
    total_score += score
    count += 1


if count > 0:
    average = total_score / count
    print("The average score is:", average)
else:
    print("No scores were entered.")
