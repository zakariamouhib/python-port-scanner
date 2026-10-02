# Python Port Scanner

Simple multithreaded TCP port scanner written in Python.

> **Disclaimer:** Educational purposes only. Only scan machines you own
> or have explicit permission to test. Unauthorized scanning may be illegal.

## Features

- Multithreaded scanning (fast)
- Custom port range
- Adjustable timeout
- Banner grabbing (detects the service on open ports)
- Save results to a file
- No external dependencies (standard library only)

## Requirements

- Python 3.8+

## Usage

    python scanner.py -t 127.0.0.1
    python scanner.py -t 127.0.0.1 -p 1-1000
    python scanner.py -t 127.0.0.1 -p 1-65535 --timeout 1
    python scanner.py -t 127.0.0.1 -p 1-1000 -o results.txt

## Options

| Option | Description | Default |
|--------|-------------|---------|
| -t, --target | Target host (required) | - |
| -p, --ports | Port range, ex: 1-1000 | 1-1024 |
| --timeout | Timeout per port (seconds) | 0.5 |
| -o, --output | Save results to a file | - |

## Example output

    [+] Port 80 open | HTTP/1.0 200 OK
    [+] Port 135 open
    [+] Port 445 open

## What I learned

- TCP sockets in Python
- Multithreading with threading
- Building a CLI with argparse
- Banner grabbing
- Git and GitHub workflow

## Roadmap

- [x] Banner grabbing
- [x] Save results to file
- [ ] Service detection (beyond HTTP)
- [ ] UDP scanning

## License

MIT
