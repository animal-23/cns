def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

message = "Hello world"
shift = 3 

encrypted_message = encrypt(message, shift)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted:", decrypted_message)

