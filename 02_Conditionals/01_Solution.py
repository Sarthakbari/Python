# take input from user 
age = int(input("Enter Your age: "))

if (age < 13):
    print("You are Child")
elif(age < 20):
    print("You are a Teenager")
elif(age < 60):
    print("Your a Adult")
else:
    print("You are a senior")
print(age)