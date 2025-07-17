import os
with open("web.txt", "r") as file:
    for website in file:
        print("=" * 30)
        print(f"Pinging {website.strip()}...")
        os.system("ping -c 2 " + website.strip())

