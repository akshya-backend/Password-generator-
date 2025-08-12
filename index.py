import random
import string

def generate_password(length, use_symbols, use_numbers, use_uppercase):
    characters = string.ascii_lowercase
    mandatory_chars = []

    if use_uppercase:
        characters += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))

    if use_numbers:
        characters += string.digits
        mandatory_chars.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))

    remaining_length = length - len(mandatory_chars)
    password_chars = mandatory_chars + [random.choice(characters) for _ in range(remaining_length)]

    random.shuffle(password_chars)
    return ''.join(password_chars)

def password_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    types_count = sum([has_upper, has_digit, has_symbol])  # lowercase assumed always present

    if length < 8 or types_count == 0:
        return "Weak"
    elif length >= 10 and types_count >= 2:
        return "Strong"
    else:
        return "Medium"

# ------------------- INPUT HELPERS -------------------
def get_length():
    while True:
        try:
            length = int(input("Enter password length (6-20): "))
            if length < 6 or length > 20:
                print("❌ Error: Length must be between 6 and 20.")
                continue
            return length
        except ValueError:
            print("❌ Please enter a valid number.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt + " (yes/no): ").strip().lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        print("❌ Please type 'yes' or 'no'.")

# ------------------- MAIN -------------------
length = get_length()
use_symbols = get_yes_no("Include symbols?")
use_numbers = get_yes_no("Include numbers?")
use_uppercase = get_yes_no("Include uppercase letters?")

password = generate_password(length, use_symbols, use_numbers, use_uppercase)
strength = password_strength(password)

print("\n✅ Generated Password:", password)
print(f"🔒 Password Strength: {strength}")

