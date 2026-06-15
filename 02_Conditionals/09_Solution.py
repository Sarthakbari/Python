# Leap Year Checker
# Determine If a year is a leap year. (Leap year are divisible by 4, but not by 100 unless also divisible by 400)

year = 2024

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This is a Leap year...", year)
else:
    print("This is not Leap year...", year)

print(year)
