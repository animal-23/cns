import hashlib
def calculate_md5_digest(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
text = input("Enter text to calculate MD5 message digest: ")
message_digest = calculate_md5_digest(text)
print("MD5 Message Digest:", message_digest)