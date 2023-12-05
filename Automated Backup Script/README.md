# Overview
This Python script automates the backup of specified directories to a designated backup location. It includes features like scheduling, compression, and error handling.
# Prerequisites
The script uses the `schedule` library, which you can install using:
```
pip install schedule
```
# Usage
1. Clone or download the repository to your local machine.
2. Open the script in a text editor.
3. Replace `/path/to/source` and `/path/to/backup` with the actual paths of the directories you want to back up and the location where you want to store the backups.
4. Open a terminal in the project directory.

To run the script:
```
python backup_script.py
```
# Running Forever and Termination
* The script is designed to run forever in the background, continuously checking for the scheduled task. Once you run it, it will keep performing the backup task every day at 2:00 AM.

* To terminate the script, you can press Ctrl+C in the terminal where the script is running. This keyboard shortcut interrupts the running process and stops the script. After termination, the script won't be actively checking for backups until you run it again.

Make sure to customize the script according to your needs

# Author
**Ahnaf Tahmid Zaman**

<a href="https://www.linkedin.com/in/ahnaf-tahmid-zaman/">
    <img src="https://dl.dropboxusercontent.com/scl/fi/6wwu1stsm3hki3vsxl5c0/linkedin.png?rlkey=4nfdo2u3tmoaxo9xwkxh6t5to&dl=0" alt="Linkedin" width="67px">
</a>
<a href="https://github.com/AHNAF14924">
    <img src="https://dl.dropboxusercontent.com/scl/fi/bys8mwgtmsjobu6uk0d15/GitHub-Symbol-2149346605.png?rlkey=memfqto1ygr91gja8t3cpwwbx&dl=0" alt="GitHub" width="100px">
</a>



