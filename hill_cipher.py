keyMatrix = [[0] * 3 for _ in range(3)]
cipher = [[0] for _ in range(3)]
def keyValue(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
def encrypt(messageVector):
    for i in range(3):
        cipher[i][0] = sum(keyMatrix[i][x] * messageVector[x][0] for x in range(3)) % 26

def hillCipher(message, key):
    keyValue(key)
    while len(message) % 3 != 0:
        message += 'X'  
    cipherText = []
    for i in range(0, len(message), 3):
        messageVector = [[ord(message[j]) % 65] for j in range(i, i + 3)]
        encrypt(messageVector)
        for i in range(3):
            cipherText.append(chr(cipher[i][0] + 65))
    return "".join(cipherText)

key = input("Enter a key of length 9 (letters A-Z): ")
message = input("Enter the plaintext to encrypt: ")
cipherText = hillCipher(message.upper(), key.upper())
print("Cipher Text =", cipherText)

