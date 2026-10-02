import socket
import threading

def scan_port(host, port, open_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))
    s.close()
    if result == 0:
        open_ports.append(port)

host = input("Host (ex: 127.0.0.1): ")
open_ports = []
threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(host, port, open_ports))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for port in sorted(open_ports):
    print(f"[+] Port {port} open")