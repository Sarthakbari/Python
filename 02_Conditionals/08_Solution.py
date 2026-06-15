password = "Secure3P@ss"

if (len(password) < 6):
    strength = "Week"
elif(len(password) <= 10):
    strength = "Medium"
else:
    strength = "Strong"
print("Password Strength is:", strength)
