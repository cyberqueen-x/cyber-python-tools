import hashlib

hash_to_crack = input("Enter sha1 to crack: ")
wordlist_path = input("Enter wordlist path: ")
try:
    with open("test.txt", "r", errors = "ignore") as file:
        for word in file:
            word = word.strip()
            result = hashlib.sha1(word.encode()).hexdigest()
            if result == hash_to_crack:
                print(f'password found {word}')
                break
            else:
                print(f'password not found in wordlist')
except FileNotFoundError:
    print("where is ur file?")

