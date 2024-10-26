import psutil
import platform
from datetime import datetime
import os
import threading
import itertools
import time
from ping3 import ping

class SystemInfo:
    @staticmethod
    def get_cpu_info():
        cpu_info = {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "Max Frequency": f"{psutil.cpu_freq().max:.2f} Mhz",
            "Min Frequency": f"{psutil.cpu_freq().min:.2f} Mhz",
            "Current Frequency": f"{psutil.cpu_freq().current:.2f} Mhz",
            "CPU Usage Per Core": [f"{usage}%" for usage in psutil.cpu_percent(percpu=True)],
            "Total CPU Usage": f"{psutil.cpu_percent()}%"
        }
        return cpu_info

    @staticmethod
    def get_memory_info():
        svmem = psutil.virtual_memory()
        memory_info = {
            "Total": f"{svmem.total / (1024 ** 3):.2f} GB",
            "Available": f"{svmem.available / (1024 ** 3):.2f} GB",
            "Used": f"{svmem.used / (1024 ** 3):.2f} GB",
            "Percentage": f"{svmem.percent}%"
        }
        return memory_info

    @staticmethod
    def get_memory_hogging_processes():
        # Create a list to hold process info
        process_list = []
        
        # Iterate through all running processes
        for process in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                mem_info = process.info['memory_info']
                if mem_info:  # Check if memory_info is not None
                    rss = mem_info.rss  # Resident Set Size
                    process_list.append((process.info['name'], rss))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue  # Skip processes that can't be accessed

        # Sort the processes by memory usage (RSS) in descending order
        sorted_processes = sorted(process_list, key=lambda x: x[1], reverse=True)

        # Format the output
        formatted_processes = [
            {"Process": name, "Memory Usage": f"{mem / (1024 ** 2):.2f} MB"} 
            for name, mem in sorted_processes
        ]
        
        return formatted_processes

    @staticmethod
    def get_storage_info():
        partitions = psutil.disk_partitions()
        storage_info = []
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            storage_info.append({
                "Device": partition.device,
                "Mount Point": partition.mountpoint,
                "File System Type": partition.fstype,
                "Total Size": f"{usage.total / (1024 ** 3):.2f} GB",
                "Used": f"{usage.used / (1024 ** 3):.2f} GB",
                "Free": f"{usage.free / (1024 ** 3):.2f} GB",
                "Percentage": f"{usage.percent}%"
            })
        return storage_info

    @staticmethod
    def get_network_info():
        # Get initial network IO counters
        initial_net_io = psutil.net_io_counters()
        initial_time = time.time()
        
        # Wait for a short interval (1 second)
        time.sleep(1)
        
        # Get network IO counters again after the interval
        final_net_io = psutil.net_io_counters()
        final_time = time.time()

        # Calculate the differences
        bytes_sent = final_net_io.bytes_sent - initial_net_io.bytes_sent
        bytes_received = final_net_io.bytes_recv - initial_net_io.bytes_recv
        time_interval = final_time - initial_time
        
        # Calculate speed in Mbps
        speed_sent_mbps = (bytes_sent * 8) / (1024 ** 2 * time_interval)
        speed_received_mbps = (bytes_received * 8) / (1024 ** 2 * time_interval)

        # Basic ping to calculate packet loss
        ping_result = ping("google.com", timeout=5)  # Replace with a suitable address
        packet_loss = None
        if ping_result is None:
            packet_loss = "Packet loss detected"
        else:
            packet_loss = "No packet loss"

        network_info = {
            "Bytes Sent": f"{final_net_io.bytes_sent / (1024 ** 2):.2f} MB",
            "Bytes Received": f"{final_net_io.bytes_recv / (1024 ** 2):.2f} MB",
            "Packets Sent": final_net_io.packets_sent,
            "Packets Received": final_net_io.packets_recv,
            "Speed Sent": f"{speed_sent_mbps:.2f} Mbps",
            "Speed Received": f"{speed_received_mbps:.2f} Mbps",
            "Packet Loss": packet_loss
        }
        return network_info

    @staticmethod
    def get_system_info():
        uname = platform.uname()
        system_info = {
            "System": uname.system,
            "Node Name": uname.node,
            "Release": uname.release,
            "Version": uname.version,
            "Machine": uname.machine,
            "Processor": uname.processor,
            "Boot Time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        }
        return system_info

    @staticmethod
    def get_folder_contents(path):
        """Retrieve files and folders within a specified directory."""
        if not os.path.exists(path):
            return f"The path '{path}' does not exist."
        
        if not os.path.isdir(path):
            return f"The path '{path}' is not a directory."
        
        try:
            contents = os.listdir(path)
            return {
                "files": [f for f in contents if os.path.isfile(os.path.join(path, f))],
                "directories": [d for d in contents if os.path.isdir(os.path.join(path, d))]
            }
        except PermissionError:
            return f"Permission denied: Cannot access '{path}'"

    @staticmethod
    def find_and_inspect_folder(folder_name, start_dir="/"):
        """Interactive search session that allows inspecting folders and navigating inside matched directories."""
        
        def loading_message():
            """Print loading animation until search completes."""
            for symbol in itertools.cycle(["|", "/", "-", "\\"]):
                if not loading:
                    break
                print(f"\rSearching, please wait... {symbol}", end="")
                time.sleep(0.5)

        # Function to display folder contents interactively
        def interactive_folder_inspect(path):
            """Loop to allow nested searches within a chosen folder."""
            current_path = path
            history = []

            while True:
                print(f"\nContents of '{current_path}':")
                contents = SystemInfo.get_folder_contents(current_path)
                
                if isinstance(contents, str):  # Check if there's an error message
                    print(contents)
                    return
                
                # Display files and directories
                print("Files:")
                for i, file in enumerate(contents['files'], 1):
                    print(f"  {i}. {file}")

                print("Directories:")
                for i, folder in enumerate(contents['directories'], 1):
                    print(f"  {i + len(contents['files'])}. {folder}")
                
                # User prompt for next action
                print("\nOptions:")
                print("  1. Enter a directory number to inspect")
                print("  2. Enter '..' to go back to the previous directory")
                print("  3. Enter 'exit' to end the search session")
                
                choice = input("Enter your choice: ")
                
                if choice.isdigit():  # Enter directory by number
                    choice = int(choice) - 1
                    if choice < len(contents['files']):  # File selected
                        print(f"\nYou selected a file: {contents['files'][choice]}")
                    elif choice < len(contents['files']) + len(contents['directories']):  # Directory selected
                        selected_folder = contents['directories'][choice - len(contents['files'])]
                        history.append(current_path)  # Save current path in history
                        current_path = os.path.join(current_path, selected_folder)
                    else:
                        print("Invalid selection.")
                elif choice == "..":  # Go up one directory
                    if history:
                        current_path = history.pop()  # Retrieve last directory
                    else:
                        print("You're at the starting directory.")
                elif choice.lower() == "exit":  # End session
                    print("Exiting search session.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        # Initial search for the folder
        matches = []
        loading = True
        loading_thread = threading.Thread(target=loading_message)
        loading_thread.start()
        
        try:
            for root, dirs, _ in os.walk(start_dir):
                if folder_name in dirs:
                    matches.append(os.path.join(root, folder_name))
                
                # Optional: Limit the number of results
                if len(matches) >= 10:
                    break

            loading = False
            loading_thread.join()
            print("\rSearch complete!                 ")

            if not matches:
                return f"No folder named '{folder_name}' found in the system."

            # Handle multiple matches
            if len(matches) > 1:
                print("Multiple matches found:")
                for i, match in enumerate(matches):
                    print(f"{i + 1}. {match}")
                
                choice = input("Select the folder to inspect (enter the number or press Enter to cancel): ")
                
                if choice.isdigit():
                    choice = int(choice) - 1
                    if 0 <= choice < len(matches):
                        selected_path = matches[choice]
                    else:
                        return "Invalid selection."
                else:
                    return "No selection made. Exiting."
            else:
                selected_path = matches[0]

            print(f"Starting search session in: {selected_path}")
            interactive_folder_inspect(selected_path)
        
        except Exception as e:
            loading = False
            loading_thread.join()
            return f"Error during search: {e}"

    @staticmethod
    def get_all_info():
        return {
            "System Info": SystemInfo.get_system_info(),
            "CPU Info": SystemInfo.get_cpu_info(),
            "Memory Info": SystemInfo.get_memory_info(),
            "Storage Info": SystemInfo.get_storage_info(),
            "Network Info": SystemInfo.get_network_info(),
            "Memory Hoggin Processes": SystemInfo.get_memory_hogging_processes(),
        }

# Example usage
# if __name__ == "__main__":

#     folder_name = input("Enter the name of the folder to inspect: ")
#     result = SystemInfo.find_and_inspect_folder(folder_name, start_dir="/")
#     if isinstance(result, str):
#         print(result)

#     info = SystemInfo.get_all_info()
#     for key, value in info.items():
#         print(f"{key}:\n", value, "\n")


