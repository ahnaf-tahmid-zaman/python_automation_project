import re
import getpass

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not re.search(r'[~!@#$%^&*()-_=+{}\[\]\\|;:\'",<.>/?]', password):
        return False

    return True

if __name__ == "__main__":
    password = getpass.getpass("Enter a password: ")
    if is_strong_password(password):
        print("Strong password")
    else:
        print("Weak password")
        