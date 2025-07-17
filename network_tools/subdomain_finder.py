import socket
domain = input("Enter a domain: ")
with open("subdomain.txt", "r") as file:
    for word in file:
       subdomain = word.strip() + "." + domain
       try:
           ip = socket.gethostbyname(subdomain)
           print(f"Found: {subdomain} & {ip}")
       except socket.gaierror:
           pass
