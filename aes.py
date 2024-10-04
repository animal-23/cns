from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt a message using AES (CBC mode)
def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC mode
    iv = cipher.iv  # Initialization vector
    padded_text = pad(plaintext.encode(), AES.block_size)  # Pad the plaintext
    encrypted_text = cipher.encrypt(padded_text)  # Encrypt the padded plaintext
    return iv + encrypted_text  # Return the IV concatenated with the ciphertext

# Function to decrypt a message using AES (CBC mode)
def decrypt_aes(key, encrypted_text):
    iv = encrypted_text[:AES.block_size]  # Extract the IV from the beginning
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create a new cipher object with the IV
    decrypted_padded_text = cipher.decrypt(encrypted_text[AES.block_size:])  # Decrypt the ciphertext
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)  # Unpad the decrypted text
    return decrypted_text.decode()  # Return the plaintext as a string

# Example usage
key = get_random_bytes(16)  # AES-128 key (16 bytes)
message = "Hello world"
print("Original message:", message)

# Encrypt the message
encrypted_message = encrypt_aes(key, message)
print("Encrypted message (hex):", encrypted_message.hex())

# Decrypt the message
decrypted_message = decrypt_aes(key, encrypted_message)
print("Decrypted message:", decrypted_message)

