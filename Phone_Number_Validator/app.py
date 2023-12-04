import re

def is_valid_phone_number(phone_number):
    pattern = r'^\+880-\d{4}-\d{4}-\d{2}$'
    return re.match(pattern, phone_number)

def main():
    file_name = 'phone_numbers.txt'

    with open(file_name, 'r') as file:
        lines = file.readlines()

    for idx, line in enumerate(lines, start=1):
        phone_number = line.strip()
        is_valid = is_valid_phone_number(phone_number)
        if is_valid:
            print(f"{idx}. {phone_number}")

if __name__ == "__main__":
    main()
