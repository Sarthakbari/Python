import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation into one pool of characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters and join them directly together (no spaces)
    return ''.join(random.choices(characters, k=length))

# Example usage:
my_password = generate_password(12)
print("Generated Password:", my_password)