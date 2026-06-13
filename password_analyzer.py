def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


password = input("Enter a password to check: ")
strength, suggestions = check_password_strength(password)

print(f"Password Strength: {strength}")

if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("Good job. Your password looks strong.")
