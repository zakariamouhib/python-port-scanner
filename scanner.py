import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

host = input("Host (ex: 127.0.0.1): ")
for port in range(1, 1025):
    if scan_port(host, port):
        print(f"[+] Port {port} open")