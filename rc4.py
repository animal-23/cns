def ksa(key):
    """ Key Scheduling Algorithm (KSA) """
    key_length = len(key)
    S = list(range(256))  # Initial permutation of S
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    """ Pseudo-Random Generation Algorithm (PRGA) """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4(key, plaintext):
    """ RC4 encryption/decryption """
    key = [ord(c) for c in key]  # Convert key to list of ASCII values
    S = ksa(key)  # Perform KSA to get initial S state
    keystream = prga(S)  # Generate the keystream using PRGA
    ciphertext = []
    for char in plaintext:
        val = ("%02X" % (ord(char) ^ next(keystream)))  # XOR and convert to hexadecimal
        ciphertext.append(val)
    return ''.join(ciphertext)  # Return the encrypted text as a hexadecimal string

def rc4_decrypt(key, ciphertext):
    """ RC4 decryption """
    key = [ord(c) for c in key]  # Convert key to list of ASCII values
    S = ksa(key)  # Perform KSA to get initial S state
    keystream = prga(S)  # Generate the keystream using PRGA
    
    # Convert ciphertext from hexadecimal string back to a list of integers
    ciphertext_bytes = [int(ciphertext[i:i+2], 16) for i in range(0, len(ciphertext), 2)]
    
    plaintext = []
    for byte in ciphertext_bytes:
        val = chr(byte ^ next(keystream))  # XOR with keystream and convert to character
        plaintext.append(val)
    return ''.join(plaintext)  # Return the decrypted text

# Example usage
key = "SecretKey"
plaintext = "Hello, RC4!"

# Encrypt the plaintext
encrypted_text = rc4(key, plaintext)

# Decrypt the encrypted text
decrypted_text = rc4_decrypt(key, encrypted_text)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")

