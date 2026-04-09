import re

while True:
    password = input(
        "Whats the password?(For exit press 'q')"
        "\n(The password must contain at least one uppercase letter, one number, and one special character.)"
    )
    if password.lower == "q":
        break
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"\W", password))
    is_long_enough = len(password) >= 8

    if all([has_digit, has_upper, has_special, is_long_enough]):
        print("pasword approved")
        break
    else:
        print("Weak password! Please check the requirements:")
        if not has_upper:
            print("  - Must contain at least one UPPERCASE letter")
        if not has_digit:
            print("  - Must contain at least one DIGIT")
        if not has_special:
            print("  - Must contain at least one SPECIAL CHARACTER (@, !, #, etc.)")
        if not is_long_enough:
            print("  - Password must be at least 8 characters long")
