import socket
import threading
import argparse


def grab_banner(s):
    try:
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        data = s.recv(1024).decode(errors="ignore").strip()
        return data.splitlines()[0] if data else ""
    except Exception:
        return ""


def scan_port(host, port, open_ports, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        if s.connect_ex((host, port)) == 0:
            banner = grab_banner(s)
            open_ports.append((port, banner))
    finally:
        s.close()


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
    parser.add_argument("-o", "--output",
                        help="Save results to a file (ex: results.txt)")
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

    lines = []
    for port, banner in sorted(open_ports):
        if banner:
            lines.append(f"[+] Port {port} open | {banner}")
        else:
            lines.append(f"[+] Port {port} open")

    for line in lines:
        print(line)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()