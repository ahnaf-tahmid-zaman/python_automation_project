import os
import re


def search_files_for_regex(folder_path, regex_pattern):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".txt"):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        for line_number, line in enumerate(file, 1):
                            if re.search(regex_pattern, line):
                                print(
                                    f"File: {file_path}, Line: {line_number}, Content: {line.strip()}")
                except UnicodeDecodeError:
                    print(
                        f"Unable to read file: {file_path}. It's not in UTF-8 encoding.")


def main():
    folder_path = input("Enter the folder path: ")
    regex_pattern = input("Enter the regular expression to search: ")
    search_files_for_regex(folder_path, regex_pattern)


if __name__ == "__main__":
    main()
