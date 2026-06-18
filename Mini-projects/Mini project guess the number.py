import random

targeet=random.randint(1,100)

while True:
    userchoice = input("guess the targeet or Quit(Q):")
    if(userchoice == "Q"):
        break
    userchoice = int(userchoice)
    if(userchoice == targeet):
        print("Success: correct Guess")
        break
    elif(userchoice < targeet):
        print("Your Number is too Small. Take a bigger guess...")
    else:
        print("Your Number is too Big. Take a smaller guess...")
print("-------Game is Over-------")
