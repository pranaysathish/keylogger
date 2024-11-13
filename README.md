# Keylogger Project

This is a Python-based keylogger application designed for educational purposes. The project demonstrates the potential risks and security threats posed by keyloggers. The keylogger captures keystrokes, clipboard content, system information, audio, and screenshots, and sends them via email. Additionally, it encrypts log files for enhanced security. The goal of this project is to raise awareness about the dangers of keyloggers and to highlight the importance of securing personal data.

## Features

- **Keystroke Logging**: Records every keystroke made by the user.
- **Clipboard Capture**: Logs clipboard content (e.g., copied text).
- **System Information**: Collects and logs system details such as IP address, processor, machine type, etc.
- **Audio Recording**: Records audio from the system's microphone.
- **Screenshot Capturing**: Takes screenshots of the system at regular intervals.
- **Email Reporting**: Sends logs and captured data to a specified email address.
- **File Encryption**: Encrypts log files before sending for added security.
- **Track Cleanup**: Deletes logs after they have been sent to prevent detection.

## Files Overview

- **keylogger.py**: Contains the main functionality of the keylogger, including keylogging, clipboard capture, system information gathering, audio recording, and screenshot capture. It also sends captured data via email and encrypts files.
- **generatekey.py**: A script used to generate a unique encryption key using the `cryptography` library.
- **decryptkey.py**: Decrypts encrypted log files and stores the decrypted data in a readable format.

## Requirements

- Python 3.x
- Required libraries:
  - `cryptography`
  - `pynput`
  - `win32clipboard`
  - `requests`
  - `scipy`
  - `sounddevice`
  - `Pillow`
  - `smtplib`

You can install the required libraries using `pip`:

