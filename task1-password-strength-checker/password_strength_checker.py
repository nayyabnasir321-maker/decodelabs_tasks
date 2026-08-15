"""
DecodeLabs Industrial Training Kit - Project 1
Password Strength Checker

Goal: Classify a password as WEAK, MEDIUM, or STRONG based on:
 - Length
 - Presence of lowercase, uppercase, digits, and symbols
 - A basic check against common/leaked passwords (bonus, as suggested
   in the project brief)

Key skills practiced: string handling, conditional logic, security basics.
"""

import string

# A small sample of extremely common / leaked passwords.
# In a real tool this list would be loaded from a much bigger breach
# database (e.g. "rockyou.txt" or the HaveIBeenPwned API).
COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "696969", "shadow", "master", "666666",
    "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "pussy", "superman", "1qaz2wsx", "7777777",
}


def check_length(password: str) -> int:
    """Return a score contribution based on password length."""
    length = len(password)
    if length < 8:
        return 0            # immediate fail zone (per the "Zero Point" rule)
    elif length < 12:
        return 1
    else:
        return 2


def has_variety(password: str) -> dict:
    """Check which character classes are present (Pythonic / short-circuit style)."""
    return {
        "lower": any(char in string.ascii_lowercase for char in password),
        "upper": any(char in string.ascii_uppercase for char in password),
        "digit": any(char.isdigit() for char in password),
        "symbol": any(char in string.punctuation for char in password),
    }


def check_strength(password: str) -> tuple[str, list[str]]:
    """
    Analyze a password and return (strength_label, list_of_feedback_notes).
    Strength is WEAK, MEDIUM, or STRONG.
    """
    notes = []

    # --- Rule 1: known leaked / common passwords are always WEAK ---
    if password.lower() in COMMON_PASSWORDS:
        return "WEAK", ["This password appears in common leaked password lists."]

    # --- Rule 2: length check ---
    length_score = check_length(password)
    if length_score == 0:
        notes.append("Too short (< 8 characters) — high brute-force risk.")
    elif length_score == 1:
        notes.append("Decent length, but 12+ characters is safer.")
    else:
        notes.append("Good length.")

    # --- Rule 3: character variety check ---
    variety = has_variety(password)
    variety_score = sum(variety.values())  # 0 to 4

    if not variety["lower"]:
        notes.append("Add lowercase letters.")
    if not variety["upper"]:
        notes.append("Add uppercase letters.")
    if not variety["digit"]:
        notes.append("Add numbers.")
    if not variety["symbol"]:
        notes.append("Add symbols (e.g. !@#$%).")

    # --- Combine scores into a final classification (0-6 total) ---
    total_score = length_score + variety_score

    if length_score == 0 or total_score <= 2:
        strength = "WEAK"
    elif total_score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, notes


def display_result(password: str) -> None:
    strength, notes = check_strength(password)
    bar = {"WEAK": "[#-----]", "MEDIUM": "[###---]", "STRONG": "[######]"}

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength: {strength}  {bar[strength]}")
    print("Feedback:")
    for note in notes:
        print(f"  - {note}")


def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to check: ").strip()
        if password.lower() == "quit":
            print("Goodbye!")
            break
        if not password:
            print("Please enter a non-empty password.")
            continue
        display_result(password)


if __name__ == "__main__":
    main()
