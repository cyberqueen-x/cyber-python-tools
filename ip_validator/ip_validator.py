import ipaddress

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)
    print("✅ Valid IP:", ip_obj)
    if ip_obj.is_multicast:
        print("⚠️This IP is in multicast range, not usually used for host communication.")
    elif ip_obj.is_reserved:
        print("⚠️This is a reserved IP, not usable for public networking.")
    elif ip_obj.is_private:
        print("ℹ️This is a private IP, commonly used in LANs.")
    else:
        print("🌐This is a public IP address.")
except ValueError:
    print("❌ Invalid IP address!")
 
