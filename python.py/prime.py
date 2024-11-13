number = int(input("give a number for check if it is prime: "))

if number < 2:
    print("The number is not prime")
else:
    for i in range(2, number):
        print("The number is not prime.")
        break
    else:
        print("The number is prime")