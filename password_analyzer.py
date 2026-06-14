import random
import string
password = input("Enter a password: ")

score = 0
suggestions = []

weak_passwords = ["password", "password123", "123456", "admin", "qwerty", "letmein", "welcome"]

# Check length
if len(password) >= 8:
    print("✓ Password is at least 8 characters long.")
    score += 1
else:
    print("✗ Password is too short. Use at least 8 characters.")
    suggestions.append("Use at least 8 characters.")

# Check uppercase letters
if any(char.isupper() for char in password):
    print("✓ Password contains an uppercase letter.")
    score += 1
else:
    print("✗ Password needs at least one uppercase letter.")
    suggestions.append("Add at least one uppercase letter.")

# Check lowercase letters
if any(char.islower() for char in password):
    print("✓ Password contains a lowercase letter.")
    score += 1
else:
    print("✗ Password needs at least one lowercase letter.")
    suggestions.append("Add at least one lowercase letter.")

# Check numbers
if any(char.isdigit() for char in password):
    print("✓ Password contains a number.")
    score += 1
else:
    print("✗ Password needs at least one number.")
    suggestions.append("Add at least one number.")

# Check special characters
special_characters = "!@#$%^&*()_-+=<>?/{}[]|"

if any(char in special_characters for char in password):
    print("✓ Password contains a special character.")
    score += 1
else:
    print("✗ Password needs at least one special character.")
    suggestions.append("Add at least one special character.")

print("\nScore:", score, "/5")

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

if password.lower() in weak_passwords:
    print("\nWarning: This is a commonly used weak password.")
    print("Choose something more unique and harder to guess.")
    suggestions.append("Avoid common passwords like password123, admin, or qwerty.")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nGreat job. No suggestions needed.")

generate = input("\nWould you like me to generate a strong password? (yes/no): ")

if generate.lower() == "yes":
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    generated_password = ""

    for i in range(12):
        generated_password += random.choice(characters)

    print("\nGenerated Password:", generated_password)
else:
    print("\nNo password generated.")