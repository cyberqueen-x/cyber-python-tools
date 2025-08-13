import base64
encoded = input("msg to decode: ")
decoded = base64.b64decode(encoded).decode()
print(decoded)
