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
  - `platform`, `os`, `datetime`, `psutil`, `cpuinfo`, `socket`, `uuid`, `re` – For other system-related functionalities.

## Installation

To install and run **Project Nimbooze**, follow these steps:

1. Clone the repository:
    ```bash
   git clone https://github.com/yourusername/nimbooze.git
   cd nimbooze

2. Instll the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    python main.py