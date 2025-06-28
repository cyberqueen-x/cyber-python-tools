import hashlib
hash_to_cracker = input("[?] Enter the MD5 hash to crack: ")
wordlist_path = input("[?] Enter path to wordlist(e.g. rockyou.txt): ")
try:
    with open(wordlist_path, "r", errors = "ignore") as file:
        for word in file:
            word = word.strip()
            result = hashlib.md5(word.encode()).hexdigest()
            if result == hash_to_cracker:
                print(f"Password found: {word}")
                break
        else:
            print("[-] Password not found in wordlist.")
except FileNotFoundError:
    print("[-] wordlist file not found.")
