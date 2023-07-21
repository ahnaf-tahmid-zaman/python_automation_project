# Email and Phone Number Extractor

## Introduction

The "Email and Phone Number Extractor" is a Python script designed to read a text file, search for email addresses and phone numbers within its content, and save the extracted information into an output file in a neat tabular format. This script utilizes regular expressions (regex) to identify patterns of email addresses and phone numbers in the text.

## Requirements

- Python 3.x
- The script utilizes the "re" module, which is a standard library in Python, so there is no need to install any external libraries.

## Usage

1. Save your input text in a file named `input.txt` in the same directory as the script.
2. Run the script by executing the following command in your terminal or command prompt:

```
python script_name.py
```

3. The script will extract email addresses and phone numbers from the input file and create an output file named `output.txt` in the same directory.

## How the Script Works

### Function: `extract_emails_and_phones(input_file)`

This function reads the content of the input file and uses regular expressions to find all occurrences of email addresses and phone numbers within the text.

Parameters:

- `input_file` (str): The name of the input file containing the text to be processed.

Returns:

The function returns two lists: **emails** and **phones**, which contain all the email addresses and phone numbers found in the input file, respectively.

### Regular Expressions (Regex) Patterns:

1. **Email Pattern**:

```
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

This regex pattern is used to find email addresses within the text. It matches strings that follow the standard format of an email address.

2. **Phone Pattern**:

```
phone_pattern = r'\+880-1\d{3}-\d{4}-\d{2}'
```

This regex pattern is used to find phone numbers starting with +880-1. It matches strings that have a specific format of a phone number.

### Function: `save_file(emails, phones, output_file)`

This function takes the lists of emails and phones, along with the output filename, and saves the extracted information into a new file.

Parameters:

- **emails** (list): A list of email addresses extracted from the input file.
- **phones** (list): A list of phone numbers extracted from the input file.
- **output_file** (str): The name of the output file where the information will be saved.

Output:

The function creates a new file named `output_file` and writes the extracted email addresses and phone numbers.

### Execution

The script starts its execution within the if `if __name__ == "__main__":` block.

1. The **input_file** variable is set to `input.txt`, which specifies the input file's name.
2. The **output_file** variable is set to `output.txt`, which specifies the name of the output file.
3. The **extract_emails_and_phones(input_file)** function is called, and the extracted emails and phones are stored in the variables `extracted_emails` and `extracted_phones`.
4. The **save_file()** function is called with the extracted email and phone lists, as well as the output filename.
5. The script prints a success message: "**Emails and phone numbers have been extracted and saved to the output file**."

## Conclusion

With the "**Email and Phone Number Extractor**" script, you can quickly and efficiently extract email addresses and phone numbers from text files and store them in a structured manner for further use or analysis.
