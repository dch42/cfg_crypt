#!/usr/bin/env python3
"""Module to create a small encrypted config file for EMAIL/PW combos"""

import getpass
import os.path
import ast
from cryptography.fernet import Fernet

def gen_key():
    """Generate fernet encryption key"""
    print("Generating encryption key...")
    fernet_key = Fernet.generate_key()
    with open('.cfg.key', 'wb') as cfg_key:
        cfg_key.write(fernet_key)
    print("\033[5m==>\033[0m Key generated at ./.cfg.key\n")

def read_key():
    """Read encryption key"""
    with open('.cfg.key', 'rb') as filekey:
        raw_key = filekey.read()
        fernet_key = Fernet(raw_key)
    return fernet_key

def gen_cfg():
    """Generate configuration file"""
    print("Generating config file...")
    LOGIN = input("Please enter your login email: ")
    PW = getpass.getpass("Please enter your login password: ")
    login_info =  '{'+ f"'EMAIL': '{LOGIN}', 'PW': '{PW}'" + '}'
    return login_info

def encrypt_cfg(login_info, fernet_key):
    """Encrypt and replace raw cfg file"""
    print("\nEncrypting config file...")
    encrypted = fernet_key.encrypt(bytes(login_info, 'utf-8'))
    with open('.crypt_cfg', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print('Encryption complete.')
    print("\033[5m==>\033[0m Encrypted file saved at ./.crypt_cfg\n")


def decrypt_cfg(fernet_key):
    """Decrypt bytes and convert to cfg dict"""
    with open('.crypt_cfg', 'rb') as file:
        encrypted = file.read()
    decrypted = fernet_key.decrypt(encrypted)
    decrypted_str = decrypted.decode('utf-8')
    config_dic = ast.literal_eval(decrypted_str)
    return config_dic

if __name__ == '__main__':
    if not os.path.exists('.cfg.key'):
        print("No key detected...")
        gen_key()
    if not os.path.exists('.crypt_cfg'):
        login_info = gen_cfg()
        key = read_key()
        encrypt_cfg(login_info, key)
    key = read_key()
    cfg = decrypt_cfg(key)
