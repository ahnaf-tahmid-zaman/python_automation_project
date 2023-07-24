## Description

**File Organizer** is a simple yet powerful Python program designed to help you effortlessly organize files in a specified directory based on their file types. This tool aims to declutter your folders and make it easier to find files by sorting them into separate folders according to their extensions (e.g., PDFs, TXTs, JPGs).

## How to Use

1. Clone or download the script to your local machine.
2. Ensure you have Python 3.x installed and accessible from the command line or terminal.
3. Execute the program by running the following command:

```
python app.py
```

## Program Explanation

- The program begins by importing two Python modules, **os** and **shutil**, which provide functionalities to interact with the operating system and perform file operations.

- The main functionality is encapsulated within the `organize_files()` function, which takes a single argument, **directory_path**. This function will sort and organize the files within the specified directory.

- The first step inside the `organize_files()` function is to convert the provided **directory_path** into an absolute path using `os.path.abspath()`. This ensures that the program works correctly even if a relative path is given.

* Next, the program initializes an empty dictionary called **file_types**. This dictionary will serve as a data structure to store the file types as keys and a list of filenames for each type as values.

- The program then obtains a list of all files and directories present in the specified **directory_path** using `os.listdir()`. It iterates through each file in the list and extracts its file extension. The extracted file types are used to group files with similar extensions together.

- For instance, if you have files like "report.txt", "presentation.ppt", and "image.jpg" in the directory, the program will create separate lists for "txt", "ppt", and "jpg" file types in the **file_types** dictionary.

- Once the files are categorized based on their types, the program proceeds to create directories for each file type and moves the corresponding files into these directories. It constructs the directory path using the uppercase version of the file type and appends 's' to the end to represent the plural form (e.g., 'TXTs', 'PDFs').

- For example, all text files (e.g., "document.txt", "notes.txt") will be moved to the "TXTs" directory, while all PDF files will be moved to the "PDFs" directory.

- The program ensures that directories are only created if they do not already exist using `os.path.exists()` and `os.makedirs()` functions.

## Running the Program

When you run the program, it will prompt you to enter the directory path you want to organize. Simply provide the absolute or relative path of the target directory, and the file organizer will do the rest.

Note

- Only files with valid extensions will be considered during the organization process. Directories or files without extensions will be ignored.
- The program assumes that you have proper read and write permissions for the provided directory.
