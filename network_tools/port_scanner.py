import socket
IP = input("Enter ip address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
print(f"\nScanning {IP} from port {start_port} to port {end_port}...\n")
for port in range(start_port, end_port+1):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((IP, port))
        if result == 0:
            print(f"port {port} is open")
            try:
                s.send(b'Hello\r\n')
                banner = s.recv(1024)
                print(f"Banner:{banner.decode().strip()}")
            except:
                print("Banner is not available")
        s.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        break
    except socket.error:
        print("socket error!")
        break

