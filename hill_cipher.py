# Initialize matrices
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipher = [[0] for i in range(3)]

# Function to generate the key matrix from the key string
def keyValue(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to encrypt the message
def encrypt(messageVector):
    # Perform matrix multiplication between keyMatrix and messageVector
    for i in range(3):
        for j in range(1):
            cipher[i][j] = 0
            for x in range(3):
                cipher[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipher[i][j] = cipher[i][j] % 26

# Hill Cipher function to process the message and key
def hillCipher(message, key):
    # Generate the key matrix
    keyValue(key)
    
    # Generate the message vector from the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    
    # Encrypt the message vector
    encrypt(messageVector)
    
    # Generate the ciphertext from the cipher matrix
    cipherText = []
    for i in range(3):
        cipherText.append(chr(cipher[i][0] + 65))
    
    # Print the ciphertext
    print("Cipher Text = ", "".join(cipherText))

# Example usage
message = "SHR"  # Message must be of length 3
key = "HGFDSAEWQ"  # Key must be of length 9 (3x3 matrix)
hillCipher(message, key)

