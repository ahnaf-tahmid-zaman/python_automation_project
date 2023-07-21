import re

def extract_emails_and_phones(input_file):
    with open(input_file, 'r') as file:
        content = file.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+880-1\d{3}-\d{4}-\d{2}'

    emails = re.findall(email_pattern, content)
    phones = re.findall(phone_pattern, content)

    return emails, phones

def save_file(emails, phones, output_file):
    with open(output_file, 'w') as file:
        file.write("Email\t\t\tPhone\n")
        for email, phone in zip(emails, phones):
            file.write(f"{email}\t{phone}\n")

if __name__ == "__main__":
    input_file = "input.txt"  
    output_file = "output.txt"
    extracted_emails, extracted_phones = extract_emails_and_phones(input_file)
    save_file(extracted_emails, extracted_phones, output_file)

    print("Emails and phone numbers have been extracted and saved to the output file.")

