from utils import SystemInfo
from utils import NoteTaking  # Import the note-taking utility

def main():
    while True:
        print("\n--- System Information and Note-Taking Menu ---")
        print("all - Get All System Info")
        print("cpu - Get CPU Info")
        print("mem - Get Memory Info")
        print("stor - Get Storage Info")
        print("net - Get Network Info")
        print("folder - Find and Inspect a Folder")
        print("proc - Get Memory Hogging Processes")
        print("notes - Access Note-Taking Utility")
        print("exit - Exit")

        choice = input("Select an option: ")

        if choice == 'all':
            info = SystemInfo.get_all_info()
            for key, value in info.items():
                print(f"{key}:\n", value, "\n")

        elif choice == 'cpu':
            cpu_info = SystemInfo.get_cpu_info()
            print("CPU Info:\n", cpu_info, "\n")

        elif choice == 'mem':
            memory_info = SystemInfo.get_memory_info()
            print("Memory Info:\n", memory_info, "\n")

        elif choice == 'stor':
            storage_info = SystemInfo.get_storage_info()
            print("Storage Info:\n", storage_info, "\n")

        elif choice == 'net':
            network_info = SystemInfo.get_network_info()
            print("Network Info:\n", network_info, "\n")

        elif choice == 'folder':
            folder_name = input("Enter the name of the folder to inspect: ")
            result = SystemInfo.find_and_inspect_folder(folder_name, start_dir="/")
            print(result)

        elif choice == 'proc':
            hogging_processes = SystemInfo.get_memory_hogging_processes()
            print("Memory Hogging Processes:\n", hogging_processes, "\n")

        elif choice == 'notes':
            note_taking_menu()

        elif choice == 'exit':
            print("Exiting the program.")
            break  # Exit the loop and the program

        else:
            print("Invalid option. Please select a valid option.")

def note_taking_menu():
    """Submenu for managing notes."""
    while True:
        print("\n--- Note-Taking Utility ---")
        print("add - Add a note")
        print("list - List notes")
        print("mark - Mark a note as done")
        print("del - Delete a note")
        print("back - Return to main menu")

        choice = input("Choose an option (1-5): ")

        if choice == "add":
            text = input("Enter your note: ")
            NoteTaking.add_note(text)
        elif choice == "list":
            NoteTaking.list_notes()
        elif choice == "mark":
            try:
                index = int(input("Enter the note number to mark as done: ")) - 1
                NoteTaking.mark_as_done(index)
            except ValueError:
                print("Invalid input. Please enter a valid note number.")
        elif choice == "del":
            try:
                index = int(input("Enter the note number to delete: ")) - 1
                NoteTaking.delete_note(index)
            except ValueError:
                print("Invalid input. Please enter a valid note number.")
        elif choice == "back":
            break  # Exit note-taking menu to return to the main menu
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
