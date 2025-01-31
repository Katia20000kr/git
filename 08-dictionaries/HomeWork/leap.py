
year = int(input("Enter a year: "))

# Check a leap year
if year % 4 != 0:
    print(f"{year} is NOT a leap year.")
elif year % 100 != 0:
    print(f"{year} IS a leap year.")
elif year % 400 == 0:
    print(f"{year} IS a leap year.")
else:
    print(f"{year} is NOT a leap year.")
