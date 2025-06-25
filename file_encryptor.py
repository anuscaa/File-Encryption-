import os

def caesar_encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def encrypt_file(filename, key):
    with open(filename, 'r') as file:
        content = file.read()

    encrypted_content = caesar_encrypt(content, key)

    encrypted_filename = f"{filename}.enc"
    with open(encrypted_filename, 'w') as file:
        file.write(encrypted_content)

    print(f"Encrypted file saved as {encrypted_filename}")

def decrypt_file(filename, key):
    with open(filename, 'r') as file:
        content = file.read()

    decrypted_content = caesar_decrypt(content, key)

    decrypted_filename = filename.replace('.enc', '.dec')
    with open(decrypted_filename, 'w') as file:
        file.write(decrypted_content)

    print(f"Decrypted file saved as {decrypted_filename}")

if __name__ == "__main__":
    print("=== File Encryption App ===")
    choice = input("Enter E to encrypt or D to decrypt: ").upper()
    filename = input("Enter the file path: ")
    key = int(input("Enter the key (number): "))

    if not os.path.exists(filename):
        print("File not found.")
    elif choice == 'E':
        encrypt_file(filename, key)
    elif choice == 'D':
        decrypt_file(filename, key)
    else:
        print("Invalid choice.")
