distance = int(input("Enter a distance:"))

if (distance < 3):
    print("There No Transportation so go walk")
elif(distance <= 15):
    print("You have bike so you can go through Bike")
else:
    print("You have car so you can go through car")
print(distance)