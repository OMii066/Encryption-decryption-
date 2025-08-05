# 🔐 Python File Encryptor / Decryptor

This is a simple Python script to **encrypt and decrypt any file** using symmetric encryption (`Fernet`).

## 🚀 Features

- Generate a secret key  
- Encrypt any file into `.enc`  
- Decrypt encrypted files using the key  

## 🧪 How to Use

1. Install cryptography:
```bash
pip install cryptography
```

2. Run the script:
```bash
python file_encryptor.py
```
Menu Options:

1: Generate a key (saves as key.key)

2: Encrypt a file (must have key.key)

3: Decrypt a file (must use the same key used to encrypt)



---

📁 Example

🔐 File Encryptor/Decryptor
1. Generate Key
2. Encrypt File
3. Decrypt File
Choose: 2
Enter filename to encrypt: secret.txt
✅ Encrypted file saved as: secret.txt.enc

Choose: 3
Enter filename to decrypt (with .enc): secret.txt.enc
✅ Decrypted file saved as: secret.txt.dec


---

⚠️ Notes

Do not delete or share your key.key — it's required to decrypt files

This tool uses symmetric encryption (same key for encryption and decryption)



---

🛠️ Requirements

Python 3.x

cryptography module


Install the module using:

pip install cryptography
