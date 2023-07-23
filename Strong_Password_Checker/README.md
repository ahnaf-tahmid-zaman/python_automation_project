# Strong Password Checker

## Description

The Strong Password Checker is a Python program designed to assess the strength of user-provided passwords. It verifies whether the input password meets specific criteria for being considered strong or weak. The program helps enhance security by encouraging users to create robust passwords, which are less vulnerable to hacking attempts.

## Usage

- Clone or download the script to your local machine.
- Ensure you have Python 3.x installed and accessible from the command line or terminal.
- Execute the program by running the following command:

```
python app.py
```

Alternatively, run the script in an integrated development environment (IDE) like PyCharm, Visual Studio Code, or IDLE.

## Features

1. Password Length: The program checks if the password is at least 8 characters long, promoting the use of longer passwords for increased security.

2. Character Variety: It verifies that the password contains both uppercase and lowercase letters, encouraging a mix of character cases.

3. Digit Inclusion: The program ensures that the password includes at least one digit (0-9) to enhance complexity.

4. Special Characters: It validates whether the password contains at least one special character from the set: `~!@#$%^&\*()-\_=+{}[]|;:'",<.>/?.`

## Output

- After entering the password, the program will display "Strong password" if it meets all the criteria.
- If the password fails to meet any of the requirements, it will show "Weak password."
