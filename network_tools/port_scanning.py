import socket
import threading
import json
def scan_port(IP, port, scan_results, lock):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((IP, port))

        if result == 0:
            banner = ""
            try:
                if port == 80 or port == 443:
                    http_request = f"""GET / HTTP/1.1\r
Host: {IP}\r
User-Agent: cyber-python-tools\r
Connection: close\r\n\r\n"""
                    s.send(http_request.encode())
                    banner = s.recv(1024).decode(errors="ignore")
                else:
                    s.send(b'Hello\r\n')
                    banner = s.recv(1024).decode(errors="ignore")
            except:
                banner = "Banner not available"

            # Lock for thread-safe writes
            with lock:
                print(f"Port {port} is open")
                print(f"Banner: {banner.strip()}\n")
                scan_results[port] = banner.strip()

        s.close()

    except socket.error:
        pass


# ✅ Main logic
IP = input("Enter IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
print(f"\nScanning {IP} from port {start_port} to {end_port}...\n")

scan_results = {}
threads = []
lock = threading.Lock()

# ✅ Launch threads
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(IP, port, scan_results, lock))
    threads.append(t)
    t.start()

# ✅ Wait for all threads to finish
for t in threads:
    t.join()

# ✅ Save results
with open("scan_results.json", "w") as outfile:
    json.dump(scan_results, outfile, indent=4)

with open("scan_results.txt", "w") as logfile:
    for port, banner in scan_results.items():
        logfile.write(f"Port {port} is open\nBanner: {banner}\n\n")

