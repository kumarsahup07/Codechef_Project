from cryptography.fernet import Fernet

# Use local path for key
KEY_PATH = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved in 'secret.key' file. Keep it safe!")

def decrypt_file(input_file, output_file):
    try:
        with open(KEY_PATH, "rb") as key_file:
            key = key_file.read()

        cipher = Fernet(key)
        
        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        
        print("File decrypted successfully!")
    except FileNotFoundError:
        print("Key file not found! Please generate the key first.")
    except Exception as e:
        print("Decryption failed:", e)

def encrypt_file(input_file, output_file):
    try:
        with open(KEY_PATH, "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        
        with open(input_file, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)
        
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
        
        print("File encrypted successfully!")
    except FileNotFoundError:
        print("Key file not found! Please generate the key first.")
    except Exception as e:
        print("Encryption failed:", e)

def user_choice():
    while True:
        print("\nFile Encryption Tool")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number (1–4).")
            continue
        
        if choice == 1:
            generate_key()
        elif choice == 2:
            input_file = input("Enter the file to encrypt: ")
            output_file = input("Enter the output file name: ")
            encrypt_file(input_file, output_file)
        elif choice == 3:
            input_file = input("Enter the file to decrypt: ")
            output_file = input("Enter the output file name: ")
            decrypt_file(input_file, output_file)
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    print("Welcome to File Encryption Tool!\n")
    user_choice()