users = {"hacker987": "r00t&5h3ll", "money": "cyber@000", "medusa": "brute@123"}
username = input("Enter username: ")
password = input("Enter password: ")
try:
    if username in users  and users[username] == password:
        print("access granted!")
    else:
        print("access denied, invalid credentials!")
except:
    print("error found!")

