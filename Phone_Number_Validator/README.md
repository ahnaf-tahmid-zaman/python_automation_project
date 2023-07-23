# Phone number validation script

## Overview

This Python script serves as an example of pattern matching using regular expressions to validate phone numbers. It reads phone numbers from a text file, validates them against a specific pattern, and prints the valid phone numbers along with their corresponding index numbers.

## Requirements

- Python 3.x
- Regular Expression Library (re)

## Functionality

The script introduces the concept of pattern matching using regular expressions. It demonstrates how to use regular expression patterns to check if phone numbers adhere to a specific format. Regular expressions (regex) are powerful tools for pattern matching in strings, and they provide a flexible way to define complex patterns.

## How Pattern Matching Works

The script includes a function `is_valid_phone_number(phone_number)` that uses regular expressions to define the valid phone number pattern. The pattern, represented by the raw string literal `r'^\+880-\d{4}-\d{4}-\d{2}$'`, describes the acceptable phone number format as +880-XXXX-XXXX-XX, where X represents any digit (0-9). The following is an explanation of the pattern components:

- `^`: Indicates the start of the string.
- `\+880`: Matches the country code +880 literally.
- `-`: Matches the hyphen character (-) literally.
- `\d{4}`: Matches exactly four digits (0-9).
- `\d{2}`: Matches exactly two digits (0-9).
- `$`: Indicates the end of the string.

The `re.match()` function checks if a phone number adheres to the defined pattern. If there is a match, it returns a match object; otherwise, it returns `None`.

## Input

The input for this script is a text file named `phone_numbers.txt`, which should be present in the same directory as the script. The file should contain phone numbers, each on a separate line, in different formats. Some of these phone numbers may conform to the defined pattern, while others may not.

## Output

The script prints the valid phone numbers and their corresponding index numbers in the format:

```
12. +880-1888-8888-88
13. +880-9999-0000-99
17. +880-1555-5555-55
```

Please note that only the valid phone numbers that match the specified pattern are printed, along with their index numbers. Phone numbers that do not match the pattern are not printed.

## Learning

By studying this script, users can learn the following concepts:

- Understanding the basics of regular expressions and their importance in pattern matching.
- Creating regular expression patterns to validate phone numbers or other specific formats.
- Utilizing the `re.match()` function to check if a string matches a given regular expression pattern.
- Implementing file input/output (I/O) operations in Python to read and process data from external files.
