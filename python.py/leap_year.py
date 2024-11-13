year = int(input("Give a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year,", year, "Leap year.")
        else:
            print("The year,", year, "Not leap year.")
    else:
        print("The year,", year, "Leap year.")
else:
    print("The year,", year, " Not leap year.")
