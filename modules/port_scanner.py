import socket

def run():
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]

    print(f"[*] Scanning {target}...\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
        sock.close()
