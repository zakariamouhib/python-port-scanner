import socket
import threading
import argparse

def scan_port(host, port, open_ports, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    if result == 0:
        open_ports.append(port)

def main():
    parser = argparse.ArgumentParser(
        description="Simple multithreaded port scanner (educational use only)"
    )
    parser.add_argument("-t", "--target", required=True,
                        help="Target host (ex: 127.0.0.1)")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Port range (ex: 1-1000)")
    parser.add_argument("--timeout", type=float, default=0.5,
                        help="Timeout per port in seconds")
    args = parser.parse_args()

    start, end = map(int, args.ports.split("-"))

    open_ports = []
    threads = []

    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port,
                             args=(args.target, port, open_ports, args.timeout))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for port in sorted(open_ports):
        print(f"[+] Port {port} open")

if __name__ == "__main__":
    main()