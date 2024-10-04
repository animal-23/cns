def caeser(st,s):
    result=""
    for i in range(len(st)):
        char=st[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s- 97) % 26 + 97)
    return result
st="HELLO"
s=3
print ("Text : " + st)
print ("Shift : " + str(s))
print ("Cipher: " + caeser(st,s))
