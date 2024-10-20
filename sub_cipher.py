import string
import random

def encrypt(text):
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    cipher_key = dict(zip(alphabet, shuffled_alphabet))
    encrypted_text = ''.join(cipher_key.get(char, char) for char in text.lower())
    return encrypted_text, cipher_key

def decrypt(text, cipher_key):
    reversed_cipher_key = {v: k for k, v in cipher_key.items()}
    decrypted_text = ''.join(reversed_cipher_key.get(char, char) for char in text.lower())
    return decrypted_text


plaintext = "hello world"
encrypted_text, cipher_key = encrypt(plaintext)
decrypted_text = decrypt(encrypted_text, cipher_key)
print("Plaintext:", plaintext)
print("Encrypted:",encrypted_text)
print("Decrypted:",decrypted_text)
