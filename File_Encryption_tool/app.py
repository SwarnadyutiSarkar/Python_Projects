from cryptography.fernet import Fernet
import os

# Generate or load encryption key
def load_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        return key

# Encrypt a file
def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    encrypted_data = fernet.encrypt(data)
    
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"File {input_file} encrypted and saved as {output_file}.")

# Decrypt a file
def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)
    
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    
    print(f"File {input_file} decrypted and saved as {output_file}.")

if __name__ == '__main__':
    key_file = 'encryption_key.key'
    
    key = load_key(key_file)
    
    while True:
        print("\nFile Encryption Tool")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_file = input("Enter path to file to encrypt: ")
            output_file = input("Enter path to save encrypted file: ")
            encrypt_file(key, input_file, output_file)
        
        elif choice == '2':
            input_file = input("Enter path to file to decrypt: ")
            output_file = input("Enter path to save decrypted file: ")
            decrypt_file(key, input_file, output_file)
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")
