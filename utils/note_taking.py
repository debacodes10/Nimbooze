import json
from datetime import datetime

class NoteTaking:
    FILE_PATH = "notes.json"

    @staticmethod
    def load_notes():
        try:
            with open(NoteTaking.FILE_PATH, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if file not found or empty

    @staticmethod
    def save_notes(notes):
        with open(NoteTaking.FILE_PATH, "w") as file:
            json.dump(notes, file, indent=4)

    @staticmethod
    def add_note(text):
        notes = NoteTaking.load_notes()
        note = {
            "text": text,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "pending"
        }
        notes.append(note)
        NoteTaking.save_notes(notes)
        print("Note added successfully!")

    @staticmethod
    def list_notes():
        notes = NoteTaking.load_notes()
        if not notes:
            print("No notes available.")
        for i, note in enumerate(notes, 1):
            status_icon = "✔" if note["status"] == "done" else "✖"
            print(f"{i}. [{status_icon}] {note['text']} (added on {note['timestamp']})")

    @staticmethod
    def mark_as_done(index):
        notes = NoteTaking.load_notes()
        if 0 <= index < len(notes):
            notes[index]["status"] = "done"
            NoteTaking.save_notes(notes)
            print("Note marked as done.")
        else:
            print("Invalid note index.")

    @staticmethod
    def delete_note(index):
        notes = NoteTaking.load_notes()
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            NoteTaking.save_notes(notes)
            print(f"Deleted note: '{deleted_note['text']}'")
        else:
            print("Invalid note index.")

# if __name__ == "__main__":
#     while True:
#         print("\n--- Note Taking Utility ---")
#         print("1. Add a note")
#         print("2. List notes")
#         print("3. Mark a note as done")
#         print("4. Delete a note")
#         print("5. Exit")

#         choice = input("Choose an option (1-5): ")
#         if choice == "1":
#             text = input("Enter your note: ")
#             NoteTaking.add_note(text)
#         elif choice == "2":
#             NoteTaking.list_notes()
#         elif choice == "3":
#             try:
#                 index = int(input("Enter the note number to mark as done: ")) - 1
#                 NoteTaking.mark_as_done(index)
#             except ValueError:
#                 print("Invalid input. Please enter a valid note number.")
#         elif choice == "4":
#             try:
#                 index = int(input("Enter the note number to delete: ")) - 1
#                 NoteTaking.delete_note(index)
#             except ValueError:
#                 print("Invalid input. Please enter a valid note number.")
#         elif choice == "5":
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
