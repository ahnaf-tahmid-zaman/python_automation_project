import platform
import os
import psutil

def get_system_information():
    system_info = {}

    # Get basic system information
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    # Get OS details
    system_info['OS'] = os.name

    # Get CPU information using psutil
    cpu_info = psutil.cpu_freq()
    system_info['CPU'] = {
        'Cores': psutil.cpu_count(logical=False),
        'Threads': psutil.cpu_count(logical=True),
        'Frequency (MHz)': cpu_info.current,
        'Architecture': platform.architecture()[0],
    }

    # Get memory information using psutil
    memory_info = psutil.virtual_memory()
    system_info['Memory'] = {
        'Total (MB)': memory_info.total // (1024 * 1024),
        'Available (MB)': memory_info.available // (1024 * 1024),
        'Used (MB)': memory_info.used // (1024 * 1024),
        'Percentage Used': memory_info.percent,
    }

    return system_info

def display_system_information(system_info):
    print("System Information:")
    for category, details in system_info.items():
        print(f"\n{category}:\n")
        if isinstance(details, dict):
            for key, value in details.items():
                print(f"{key}: {value}")
        else:
            print(details)

if __name__ == "__main__":
    system_info = get_system_information()
    display_system_information(system_info)
