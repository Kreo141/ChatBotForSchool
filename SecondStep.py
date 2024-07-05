from cryptography.fernet import Fernet

with open('encryption_key.txt', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

with open('encrypted_code.txt', 'rb') as file:
    encrypted_code = file.read()

decrypted_code = cipher_suite.decrypt(encrypted_code).decode()

exec(decrypted_code)
