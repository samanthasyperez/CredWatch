# Import required libraries
import os
import re
import socket

# Patterns to identify hardcoded credentials
HARDCODED_CREDENTIALS = [
    re.compile(r'["\']?(password|passwd|pwd)["\']?\s*[:=]\s*["\'].*?["\']', re.IGNORECASE),
    re.compile(r'API[_-]?KEY\s*[:=]\s*["\'].*?["\']', re.IGNORECASE),
    re.compile(r'SECRET\s*[:=]\s*["\'].*?["\']', re.IGNORECASE),
]

# Directory to scan (root by default)
SCAN_DIR = "./"

# Scan files for hardcoded secrets
def scan_files():
    print("[+] Scanning files for hardcoded credentials...")
    for root, _, files in os.walk(SCAN_DIR):
        for file in files:
            if file.endswith(('.py', '.js', '.env', '.txt')):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', errors='ignore') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            for pattern in HARDCODED_CREDENTIALS:
                                if pattern.search(line):
                                    print(f"[!] Found potential secret in {full_path} (line {i+1}): {line.strip()}")
                except Exception as e:
                    print(f"[!] Could not read {full_path}: {e}")

# Check for exposed .env files
def check_env_files():
    print("[+] Checking for exposed .env files...")
    if os.path.exists(".env"):
        print("[!] .env file found in project root — ensure it's in .gitignore and not uploaded!")

# Scan for open common ports on localhost
def check_open_ports():
    print("[+] Checking for open common ports on localhost...")
    common_ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        6379: "Redis",
        27017: "MongoDB"
    }
    for port, service in common_ports.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                print(f"[!] Port {port} ({service}) is open on localhost")

# Main entry point
if __name__ == '__main__':
    print("==== Scan Starting ====")
    scan_files()
    check_env_files()
    check_open_ports()
    print("==== Scan Complete ====")
