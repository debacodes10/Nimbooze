# Project Nimbooze

**Project Nimbooze** is a lightweight and friendly utility tool designed to streamline everyday tasks. It integrates control for media (music, video), browser management, note-taking, and system information retrieval, all in one place. 

## Features

1. **Media Controls**
   - Control local music and video files (`mp3/mp4`).
   - Manage browser-based media playback (YouTube).
   - Control Spotify music playback.

2. **Browser Control**
   - Automate browser operations such as tab searching, and performing keystroke actions.
   
3. **Short Note Taking**
   - Easily create, store, and manage short notes for quick reference.
   
4. **System Information**
   - Retrieve memory, storage, and CPU information.
   - Display file structure and directory information.

## Libraries and Dependencies

- **Media and Browser Control**
  - `pygame` – For controlling local media files.
  - `playwright/selenium` – For browser automation.
  - `pyautogui` – For keystroke actions and system control.
  - `pynput` – For listening and controlling input devices (keyboard, mouse).
  - `sikuli` – For visual automation where needed.

- **Note Taking**
  - Basic file I/O operations for storing and managing `.txt` files.

- **System Information**
  - `psutil` – For retrieving system-related information (memory, CPU, storage).
  - `platform`, `os`, `datetime`, `cpuinfo`, `socket`, `uuid`, `re` – For other system-related functionalities.

## Installation

To install and run **Project Nimbooze**, follow these steps:

1. Clone the repository:
    ```bash
   git clone https://github.com/debacodes10/nimbooze.git
   cd nimbooze

2. Instll the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    python main.py


## Usage

- Media Controls: Control music and video files from your local system or your browser.
- Browser Automation: Switch between tabs, search for content in tabs, and perform keystrokes automatically.
- Note Taking: Create and store notes in a simple and fast way using text files.
- System Information: Access memory, storage, and CPU usage information with simple commands.

## Directory Structure

Nimbooze/
│
├── nimbooze/                   # Core application code
│   ├── media_control.py       # Controls local media and Spotify playback
│   ├── browser_control.py     # Controls browser tabs and operations
│   ├── note_manager.py        # Handles note-taking functionality
│   ├── system_info.py         # Retrieves system-related information
│   └── __init__.py
│
├── utils/                     # Utility functions and helpers
│   ├── config.py              # Configuration settings
│   ├── logger.py              # Logging functionality
│   └── helpers.py             # Additional helper functions
│
├── tests/                     # Test cases for the project
│   └── test_nimbooze.py         # Unit tests
│
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
└── main.py                    # Entry point for running the application

## Future Plans

- Voice Command Integration: Add voice commands to control media and system operations.
- Task Scheduler: Automatically perform scheduled tasks like system cleanups or note reminders.
- Cross-Platform Support: Make Nimbus run smoothly on different operating systems (Windows, MacOS, Linux).

## Contribution

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for suggestions and improvements.

## License

This project is not licensed yet and is free to use!

### Made with ❤️ by Debadyuti Mukherjee