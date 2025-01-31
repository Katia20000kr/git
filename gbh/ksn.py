# Ζητάμε από τον χρήστη να εισάγει έναν αριθμό
N = int(input("Enter number: "))

# Υπολογίζουμε το γινόμενο όλων των αριθμών από το 1 μέχρι το N
product = 1
for i in range(1, N + 1):
    product *= i

# Εμφανίζουμε το αποτέλεσμα
print("Sum is:", product)
