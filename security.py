import re


def check_password_strength(password):
    """
    Checks the strength of a password based on specific criteria:
    - At least 1 uppercase letter
    - At least 1 digit
    - At least 1 special character
    - Minimum length of 8 characters
    """
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"\W", password))
    is_long_enough = len(password) >= 8

    if all([has_digit, has_upper, has_special, is_long_enough]):
        return True
    else:
        return False


if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    user_input = input("Enter a password to test: ")

    if check_password_strength(user_input):
        print("Success: Strong password!")
    else:
        print("Error: Weak password!")
        print(
            "Requirements: At least 1 uppercase, 1 digit, 1 special char, and 8+ characters."
        )
