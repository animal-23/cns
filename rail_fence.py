def encrypt_rail_fence(text, key):
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    row, direction = 0, 1
    for i in range(len(text)):
        rail[row][i] = text[i]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    encrypted_text = ''.join([''.join(row) for row in rail])
    return encrypted_text

def decrypt_rail_fence(cipher_text, key):
    rail = [['' for _ in range(len(cipher_text))] for _ in range(key)]
    row, direction = 0, 1
    for i in range(len(cipher_text)):
        rail[row][i] = '*'
        row += direction
        
        if row == 0 or row == key - 1:
            direction *= -1
    
    idx = 0
    for r in range(key):
        for c in range(len(cipher_text)):
            if rail[r][c] == '*' and idx < len(cipher_text):
                rail[r][c] = cipher_text[idx]
                idx += 1

    decrypted_text = []
    row, direction = 0, 1
    for i in range(len(cipher_text)):
        decrypted_text.append(rail[row][i])
        row += direction
        
        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(decrypted_text)

message = "HELLO RAIL FENCE CIPHER"
key = 3
encrypted = encrypt_rail_fence(message.replace(" ", ""), key)
print("Encrypted Message:", encrypted)
decrypted = decrypt_rail_fence(encrypted, key)
print("Decrypted Message:", decrypted)