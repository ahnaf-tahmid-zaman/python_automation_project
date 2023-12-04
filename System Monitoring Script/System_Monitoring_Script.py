import psutil
import platform
import datetime
import time

def get_system_info():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Get disk space usage
    disk = psutil.disk_usage('/')
    disk_space_total = disk.total
    disk_space_used = disk.used
    disk_space_percent = disk.percent

    # Get network activity
    network = psutil.net_io_counters()
    network_bytes_sent = network.bytes_sent
    network_bytes_received = network.bytes_recv

    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_space_total': disk_space_total,
        'disk_space_used': disk_space_used,
        'disk_space_percent': disk_space_percent,
        'network_bytes_sent': network_bytes_sent,
        'network_bytes_received': network_bytes_received
    }

def display_system_info(info):
    print("\nSystem Monitoring Information:")
    print(f"CPU Usage: {info['cpu_usage']}%")
    print(f"Memory Usage: {info['memory_usage']}%")
    print(f"Disk Space: {info['disk_space_used'] / (1024 ** 3):.2f} GB / {info['disk_space_total'] / (1024 ** 3):.2f} GB ({info['disk_space_percent']}%)")
    print(f"Network Activity: Sent: {info['network_bytes_sent'] / (1024 ** 2):.2f} MB, Received: {info['network_bytes_received'] / (1024 ** 2):.2f} MB")

def log_system_info(info, log_file):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - CPU: {info['cpu_usage']}%, Memory: {info['memory_usage']}%, Disk: {info['disk_space_percent']}%, Sent: {info['network_bytes_sent'] / (1024 ** 2):.2f} MB, Received: {info['network_bytes_received'] / (1024 ** 2):.2f} MB\n"
    
    with open(log_file, 'a') as f:
        f.write(log_entry)

if __name__ == "__main__":
    log_file = "system_monitoring_log.txt"

    print(f"System Monitoring Script - {platform.system()} {platform.release()}")
    
    try:
        while True:
            system_info = get_system_info()
            display_system_info(system_info)
            log_system_info(system_info, log_file)
            time.sleep(5)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("\nMonitoring script terminated by user.")
