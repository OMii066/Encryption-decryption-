# file_encryptor.py

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"✅ Encrypted file saved as: {filename}.enc")

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    original_name = filename.replace(".enc", ".dec")
    with open(original_name, "wb") as file:
        file.write(decrypted)
    print(f"✅ Decrypted file saved as: {original_name}")

# -------------------------
print("🔐 File Encryptor/Decryptor")

choice = input("1. Generate Key\n2. Encrypt File\n3. Decrypt File\nChoose: ")

if choice == '1':
    write_key()
    print("✅ Key generated and saved as 'key.key'")
elif choice == '2':
    key = load_key()
    filename = input("Enter filename to encrypt: ")
    encrypt_file(filename, key)
elif choice == '3':
    key = load_key()
    filename = input("Enter filename to decrypt (with .enc): ")
    decrypt_file(filename, key)
else:
    print("❌ Invalid choice")
