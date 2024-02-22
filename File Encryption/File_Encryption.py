"""Assignment 4: File Encryption
Create a Python script that encrypts and decrypts text files using a simple substitution cipher. 
Implement functions for encryption and decryption using a basic substitution cipher algorithm (e.g., shifting each letter by a fixed number of positions in the alphabet).
Prompt users to enter a filename and choose whether to encrypt or decrypt the file.
Ensure the script handles cases where the file does not exist or cannot be opened for reading/writing."""

with open('E:\Python-Internship-2024\File Encryption\example.txt', 'r') as file:
    text = file.read()

shift = 5

def encryption(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decryption(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# encryption
encrypted_text = encryption(text, shift)
print(encrypted_text)

# decryption
decrypted_text = decryption(encrypted_text, shift)
print(decrypted_text)