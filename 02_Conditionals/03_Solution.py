Marks = int(input("Enter Your Marks: "))
if(Marks >= 101):
    print("Please Verify your grade")
    exit()

if(Marks >= 90):
    print("Your Grade is A")
elif(Marks >= 80):
    print("Your Grade is B")
elif(Marks >= 70):
    print("Your Grade is C")
elif(Marks >= 60):
    print("Your Grade is D")
else:
    print("Your Fail")

print("You scored: ", Marks)