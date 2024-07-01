import random

def generate(length):
    if length < 4:
        print("Password length should be at least 4 characters")

    # Define the character sets
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    punctuation = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # Combine all character sets
    characters = uppercase_letters + lowercase_letters + digits + punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(punctuation),
    ]

    # Fill the rest of the password length with random choices from all characters
    password =password + random.choices(characters, k=length - 4)

    # Shuffle the result to ensure the first 4 characters aren't always in the same order
    random.shuffle(password)

    # Convert list to string
    your_password=''.join(password)
    return your_password
    

# Example usage
length=int(input("enter the required password length:\n"))
print("your password:",generate(length))