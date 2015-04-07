'''
@author Sam Abbate
Created on Mar 29, 2015

This program can encrypt a text file, or decrypt an encrypted file using AES Symmetric
Key Encryption.

'''
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

# Configure these global variables to encrypt/decrypt.
# NOTE: A file that is already encrypted will throw an error if you try to encrypt it again
FILE_NAME = 'test.txt'
KEY_ROOT = 'rootkeyhere'
ZERO_FOR_ENCRYPT_ONE_FOR_DECRYPT = 1

# This function encrypts the contents of a text file
def encrypt(filename, root):

    # Open up unencrypted file and read the plaintext into a buffer.
    with open(filename,'r') as f:
        buffer = f.read()
    plaintext = buffer

    # Create a 16 byte SHA hash of the key root
    hash = SHA256.new()
    hash.update(root.encode('utf-8'))
    key = hash.digest()[0:16]

    # Using this newly generated key, create a cipher. Then, use this cipher to encrypt
    # the plaintext
    cipher = AES.new(key, AES.MODE_CFB, 'this is an IV456')
    ciphertext = cipher.encrypt(plaintext)

    # Write the encrypted plaintext (ciphertext) into the same file.
    # NOTE: this ciphertext is written in bytes, not unicode. Notice the "wb" flag
    # in write() instead of just "w".
    with open(filename,'wb') as f:
        f.write(ciphertext);
    with open("key_"+filename,'wb') as f:
        f.write(key);

def decrypt(filename, root):

    # Open up encrypted file and read the ciphertext into a buffer.
    with open(filename, 'rb') as f:
        buffer = f.read()
    ciphertext = buffer

    # Create a 16 byte SHA hash of the key root
    with open("key_" + filename, 'rb') as f:
        buffer = f.read()
    key1 = buffer

    # Using this newly generated key, create a cipher. Then, use this cipher to decrypt
    # the ciphertext
    cipher = AES.new(key1, AES.MODE_CFB, 'this is an IV456')
    plaintext = cipher.decrypt(ciphertext)

    # Write the decrypted ciphertext (plaintext) into the same file.
    with open(filename,'wb') as f:
        f.write(plaintext)


if __name__ == "__main__":

    if ZERO_FOR_ENCRYPT_ONE_FOR_DECRYPT == 0:
        encrypt(FILE_NAME, KEY_ROOT)
    if ZERO_FOR_ENCRYPT_ONE_FOR_DECRYPT == 1:
        decrypt(FILE_NAME, KEY_ROOT)
