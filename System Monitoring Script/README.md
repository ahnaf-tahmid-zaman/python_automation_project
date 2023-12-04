# Overview
This Python script provides a simple system monitoring tool that collects and displays information about CPU usage, memory usage, disk space, and network activity. Additionally, it logs this information to a file for future analysis.
# Prerequisites
 The script uses the `psutil` library, which you can install using:
 ```
 pip install psutil
 ```
 # Usage
1. Clone or download the repository to your local machine.
2. Open a terminal in the project directory.

To run the script:
```
python system_monitor.py
```
# Script Behavior
1. The script gathers information about CPU usage, memory usage, disk space, and network activity at 5-second intervals (adjustable).
2. The gathered information is displayed on the console in a user-friendly format.
3. The script logs the information to a file named `system_monitoring_log.txt` in the project directory.
4. To stop the script, press `Ctrl+C`. A message will indicate that the monitoring script was terminated by the user.
