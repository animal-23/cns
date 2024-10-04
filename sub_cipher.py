import string
import random

def monoalphabetic_cipher(text, cipher_key=None, decrypt=False):
    alphabet = list(string.ascii_lowercase)
    
    # Generate a cipher key if not provided
    if cipher_key is None:
        shuffled_alphabet = alphabet[:]
        random.shuffle(shuffled_alphabet)
        cipher_key = dict(zip(alphabet, shuffled_alphabet))
    else:
        # If decrypting, reverse the cipher key
        if decrypt:
            cipher_key = {v: k for k, v in cipher_key.items()}
    
    # Encrypt or decrypt the text
    translated_text = ''.join(cipher_key.get(char, char) for char in text.lower())
    
    return translated_text, cipher_key

# Example usage
plaintext = "hello world"

# Encrypt the plaintext
encrypted_text, cipher_key = monoalphabetic_cipher(plaintext)

# Decrypt the encrypted text
decrypted_text, _ = monoalphabetic_cipher(encrypted_text, cipher_key, decrypt=True)

#print(f"Cipher Key: {cipher_key}")
print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
