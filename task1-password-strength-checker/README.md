# Password Strength Checker

This is Project 1 of my DecodeLabs Cyber Security Industrial Training (Batch 2026).
It analyzes a password and classifies it as **WEAK**, **MEDIUM**, or **STRONG** based on length, character variety, and a check against commonly leaked passwords.

## Features
- Checks password length (penalizes passwords under 8 characters)
- Checks for lowercase, uppercase, digits, and symbols
- Flags passwords found in a common/leaked password list
- Gives specific feedback on how to improve a weak password
- Displays a visual strength bar (e.g. `[###---]`)
- Runs in a loop so multiple passwords can be checked in one session

## How to Run
1. Clone this repository
2. Run the script using: `python password_strength_checker.py`
3. Enter a password when prompted
4. View the strength rating and feedback
5. Type `quit` to exit the program

## Skills Demonstrated
- String handling and validation
- Conditional logic and scoring systems
- Security fundamentals (common password / breach-list awareness)
- Python fundamentals (functions, sets, tuples, type hints)
