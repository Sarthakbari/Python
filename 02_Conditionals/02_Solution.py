age = int(input("Enter age: "))
day = "Wednesday"

# This is the shortest syntax using if-esle....
# price = 12 if age >= 18 else 8  

if(age >= 18):
    price = 12
else:
    price = 8

if (day == "Wednesday"):
    price = price - 2
    # price -= 2

print("Ticket Price For You is $", price)