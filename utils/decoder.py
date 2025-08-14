import base64
encoded = input("msg to decode: ")

try:
    decoded = base64.b64decode(encoded).decode()
    print(decoded)
except Exception as e:
    print(f"error {e} occur!")
