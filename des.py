from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Function to encrypt plaintext using DES
def encrypt(plaintext, key):
    # Create a DES cipher object in CBC mode
    cipher = DES.new(key, DES.MODE_CBC)
    
    # Pad the plaintext to be a multiple of the block size
    padded_text = pad(plaintext, DES.block_size)
    
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_text)
    
    # Return the initialization vector (IV) and the ciphertext
    return cipher.iv, ciphertext

# Function to decrypt ciphertext using DES
def decrypt(ciphertext, key, iv):
    # Create a DES cipher object in CBC mode with the provided IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted text to remove padding
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    
    # Return the decrypted plaintext as a string
    return decrypted_text

# Example usage
key = b'abcdefgh'  # Key must be exactly 8 bytes for DES
plaintext = b"Hello, World!"

# Encrypt the plaintext
iv, ciphertext = encrypt(plaintext, key)

# Display the results
print(f"Plaintext: {plaintext}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Initialization Vector (IV): {iv.hex()}")

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key, iv)

# Display the decrypted text
print(f"Decrypted text: {decrypted_text}")

