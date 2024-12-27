import re

def password_strength_checker(password):
    results = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'special_chars': False
    }

    if len(password) >= 8:
        results['length'] = True

    if re.search(r"[A-Z]", password):
        results['uppercase'] = True

    if re.search(r"[a-z]", password):
        results['lowercase'] = True

    if re.search(r"\d", password):
        results['numbers'] = True

    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        results['special_chars'] = True

    strength = 0
    for value in results.values():
        if value:
            strength += 1

    levels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong', 'Very Strong']
    level = levels[strength]

    return {
        'results': results,
        'strength': strength,
        'level': level
    }

password = input("Enter a password: ")
results = password_strength_checker(password)

print("Password Strength Results:")
print("---------------------------")
for key, value in results['results'].items():
    print(f"{key.capitalize()}: {'Yes' if value else 'No'}")

print(f"\nPassword Strength: {results['strength']}/5")
print(f"Password Level: {results['level']}")