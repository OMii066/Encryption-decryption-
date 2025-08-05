# 🔐 Python File Encryptor / Decryptor

This is a simple Python script to **encrypt and decrypt any file** using symmetric encryption (`Fernet`).

## 🚀 Features

- Generate a secret key
- Encrypt any file into `.enc`
- Decrypt encrypted files using the key

## 🧪 How to Use

1. Install cryptography:
```bash
pip install cryptography '''

2. Run the script:
'''bash
python file_encryptor.py '''

Menu Options:

1: Generate key (saves as key.key)

2: Encrypt a file (you must have key.key)

3: Decrypt a file (must use same key)


📁 Example

1. Generate Key
2. Encrypt File
3. Decrypt File
Choose: 2
Enter filename to encrypt: secret.txt
✅ Encrypted file saved as: secret.txt.enc

⚠️ Notes

Never share your key.key publicly.

This uses symmetric encryption — same key is used for both encrypting and decrypting.
