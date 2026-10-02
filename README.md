# Python Port Scanner

Simple multithreaded TCP port scanner written in Python.

> **Disclaimer:** Educational purposes only. Only scan machines you own
> or have explicit permission to test. Unauthorized scanning may be illegal.

## Features

- Multithreaded scanning (fast)
- Custom port range
- Adjustable timeout
- No external dependencies (standard library only)

## Requirements

- Python 3.8+

## Usage

    python scanner.py -t 127.0.0.1
    python scanner.py -t 127.0.0.1 -p 1-1000
    python scanner.py -t 127.0.0.1 -p 1-65535 --timeout 1

## Options

| Option | Description | Default |
|--------|-------------|---------|
| -t, --target | Target host (required) | - |
| -p, --ports | Port range, ex: 1-1000 | 1-1024 |
| --timeout | Timeout per port (seconds) | 0.5 |

## What I learned

- TCP sockets in Python
- Multithreading with threading
- Building a CLI with argparse
- Git and GitHub workflow

## Roadmap

- [ ] Banner grabbing
- [ ] Service detection
- [ ] Save results to file

## License

MIT
