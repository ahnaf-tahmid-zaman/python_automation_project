import shutil
import zipfile
import schedule
import time
import os

def backup(source_dir, backup_dir):
    try:
        # Create a backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Generate a timestamp for the backup file
        timestamp = time.strftime("%Y%m%d%H%M%S")
        backup_file = os.path.join(backup_dir, f"backup_{timestamp}.zip")

        # Create a zip file and add the contents of the source directory
        with zipfile.ZipFile(backup_file, 'w') as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname=arcname)

        print(f"Backup completed successfully: {backup_file}")

    except Exception as e:
        print(f"Error during backup: {e}")

# Schedule the backup job to run daily at a specific time (adjust as needed)
schedule.every().day.at("02:00").do(backup, source_dir='/path/to/source', backup_dir='/path/to/backup')

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
