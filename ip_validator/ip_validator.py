import ipaddress

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)
    print("✅ Valid IP:", ip_obj)
except:
    print("❌ Invalid IP address!")
