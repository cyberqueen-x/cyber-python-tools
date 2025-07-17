import os
import socket
URL = input("Enter target url: ")
print(f"pinging website {URL}")
os.system("ping -c 2 " + URL)
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
print(f"Scanning ports from port {start_port} to port {end_port} on {URL}")
for port in range(start_port, end_port+1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((URL, port))
        if result == 0:
            print(f"port {port} is open")
        s.close()
    except:
        pass

