import hashlib
def sha1_hash(message):
    sha1 = hashlib.sha1()
    sha1.update(message.encode('utf-8'))
    return sha1.hexdigest()
message = " Cryptography and network security"
hash_value = sha1_hash(message)
print("Message:", message)
print("SHA-1 Hash:", hash_value)