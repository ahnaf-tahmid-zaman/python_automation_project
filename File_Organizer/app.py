import os
import shutil

def organize_files(directory_path):
    directory_path = os.path.abspath(directory_path)
    file_types = {}
    
    # Get a list of all files in the directory
    all_files = os.listdir(directory_path)
    
    for filename in all_files:
        filepath = os.path.join(directory_path, filename)
        
        if os.path.isfile(filepath):
            file_type = filename.split('.')[-1]
            if file_type not in file_types:
                file_types[file_type] = []
            file_types[file_type].append(filename)
    
    # Create directories for each file type and move files
    for file_type, files in file_types.items():
        type_directory = os.path.join(directory_path, file_type.upper() + 's')
        
        if not os.path.exists(type_directory):
            os.makedirs(type_directory)
        
        for filename in files:
            src = os.path.join(directory_path, filename)
            dest = os.path.join(type_directory, filename)
            shutil.move(src, dest)
    
    print("File organization completed.")

if __name__ == "__main__":
    path = input("Enter the directory path to organize files: ")
    organize_files(path)
