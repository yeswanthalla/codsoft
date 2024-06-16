import random
import string

def generate_password(length):
    # Define the character sets to use for generating the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the list to ensure randomness and convert to a string
    random.shuffle(password)
    password = ''.join(password)

    return password

def main():
    print("Password Generator")
    
    # Get user input for the desired password length
    length = int(input("Enter the desired length of the password: "))

    # Ensure the password length is at least 4 characters
    if length < 4:
        print("Password length should be at least 4 characters to include a mix of character types.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

# Run the password generator
main()
