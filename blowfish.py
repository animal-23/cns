from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

# Function to encrypt a message using Blowfish
def encrypt_blowfish(key, plaintext):
    # Create a Blowfish cipher object in ECB mode
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Pad the plaintext to make it a multiple of Blowfish's block size
    padded_text = pad(plaintext.encode(), Blowfish.block_size)
    
    # Encrypt the padded plaintext
    encrypted_text = cipher.encrypt(padded_text)
    
    return encrypted_text

# Function to decrypt a message using Blowfish
def decrypt_blowfish(key, encrypted_text):
    # Create a Blowfish cipher object in ECB mode
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Decrypt the encrypted text
    decrypted_padded_text = cipher.decrypt(encrypted_text)
    
    # Unpad the decrypted text to get the original message
    decrypted_text = unpad(decrypted_padded_text, Blowfish.block_size)
    
    return decrypted_text.decode()

# Example usage
key = b'Sixteen byte key'  # Key must be between 4 and 56 bytes for Blowfish
message = "Hello world"

print("Original message:", message)

# Encrypt the message
encrypted_message = encrypt_blowfish(key, message)
print("Encrypted message (in hex):", encrypted_message.hex())

# Decrypt the message
decrypted_message = decrypt_blowfish(key, encrypted_message)
print("Decrypted message:", decrypted_message)

