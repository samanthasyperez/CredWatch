# CredWatch
Lightweight Python scanner to detect hardcoded credentials, exposed .env files, and open local ports, built for learning and application security testing.

## Information:
**CredWatch** is a beginner-friendly Python tool designed to scan your local project directory for common security issues:

- Hardcoded credentials (e.g., passwords, API keys)
- Exposed `.env` files
- Open ports on localhost for common services (MySQL, Redis, etc.)

It’s a learning-focused project to help aspiring security engineers, QA testers, and DevSecOps interns understand and detect risky practices in codebases.

---

## Features:
- Regex-based scanning of code for hardcoded secrets
- Detects `.env` files and warns about exposure
- Checks for open common ports (localhost only)
- Simple output with file names and line numbers
- Pure Python, no dependencies

---

## Steps to Use:

1. Clone the repo:
```bash
git clone https://github.com/yourusername/credwatch.git
cd credwatch
```

2. Run the scanner:
```bash
python vulnscanner.py
```

---

## What It Detects:

| Type            | Example Detected                             |
|-----------------|----------------------------------------------|
| Passwords       | `password = "admin123"`                      |
| API Keys        | `API_KEY = "sk_test_123abc"`                 |
| Secret Tokens   | `SECRET = "sensitive_token_here"`            |
| Exposed Files   | `.env` in root directory                     |
| Open Ports      | 3306 (MySQL), 6379 (Redis), 27017 (MongoDB)  |

---

## Example Output:
```
==== VulnScanner 101 ====
[+] Scanning files for hardcoded credentials...
[!] Found potential secret in ./main.py (line 23): password = "letmein"
[+] Checking for exposed .env files...
[!] .env file found in project root — ensure it's in .gitignore and not uploaded!
[+] Checking for open common ports on localhost...
[!] Port 3306 (MySQL) is open on localhost
==== Scan Complete ====
```

---

## Limitations:
- Designed for **local, educational use only**
- Regex patterns may miss edge cases or trigger false positives
- Port scan is limited to common ports on `127.0.0.1`

---
