def generate_key_matrix(key):
    # Prepare the key by removing spaces and replacing 'J' with 'I'
    key = key.replace(" ", "").upper().replace("J", "I")
    
    matrix = []
    used_chars = set()
    
    # Add unique characters from the key to the matrix
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    # Add remaining characters of the alphabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is omitted
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    # Return the key matrix in 5x5 form
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    # Find the position of a character in the key matrix
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def process_digraphs(text):
    # Prepare the text: remove spaces, replace 'J' with 'I', and create digraphs
    text = text.replace(" ", "").upper().replace("J", "I")
    
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    
    # Ensure last digraph has two characters by padding with 'X' if necessary
    if len(digraphs[-1]) == 1:
        digraphs[-1] += 'X'
    
    return digraphs

def playfair_encrypt(plaintext, key):
    # Generate key matrix and process the plaintext into digraphs
    matrix = generate_key_matrix(key)
    digraphs = process_digraphs(plaintext)
    
    ciphertext = ""
    
    for digraph in digraphs:
        a_row, a_col = find_position(digraph[0], matrix)
        b_row, b_col = find_position(digraph[1], matrix)
        
        # If both letters are in the same row
        if a_row == b_row:
            ciphertext += matrix[a_row][(a_col + 1) % 5]
            ciphertext += matrix[b_row][(b_col + 1) % 5]
        # If both letters are in the same column
        elif a_col == b_col:
            ciphertext += matrix[(a_row + 1) % 5][a_col]
            ciphertext += matrix[(b_row + 1) % 5][b_col]
        # If the letters form a rectangle, swap their columns
        else:
            ciphertext += matrix[a_row][b_col]
            ciphertext += matrix[b_row][a_col]
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    # Generate key matrix and process the ciphertext into digraphs
    matrix = generate_key_matrix(key)
    digraphs = process_digraphs(ciphertext)
    
    plaintext = ""
    
    for digraph in digraphs:
        a_row, a_col = find_position(digraph[0], matrix)
        b_row, b_col = find_position(digraph[1], matrix)
        
        # If both letters are in the same row
        if a_row == b_row:
            plaintext += matrix[a_row][(a_col - 1) % 5]
            plaintext += matrix[b_row][(b_col - 1) % 5]
        # If both letters are in the same column
        elif a_col == b_col:
            plaintext += matrix[(a_row - 1) % 5][a_col]
            plaintext += matrix[(b_row - 1) % 5][b_col]
        # If the letters form a rectangle, swap their columns
        else:
            plaintext += matrix[a_row][b_col]
            plaintext += matrix[b_row][a_col]
    
    return plaintext

# Example usage
plaintext = "HELLO WORLD"
key = "KEYWORD"

# Encrypt the plaintext
encrypted_text = playfair_encrypt(plaintext, key)

# Decrypt the ciphertext
decrypted_text = playfair_decrypt(encrypted_text, key)

# Print results
print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")

