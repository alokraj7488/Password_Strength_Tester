# Password Strength & Leak Checker 🔐

A simple yet powerful Python tool that checks:
- The strength of your password based on complexity rules
- Whether your password has been leaked using the [Have I Been Pwned](https://haveibeenpwned.com/ ) API

---

## 🔍 Features

- Checks password length, uppercase, lowercase, numbers, and special characters
- Detects weak patterns and repeated characters
- Rates password as **Weak**, **Moderate**, or **Strong**
- Verifies if the password was ever exposed in data breaches (via SHA-1 hashing)
- Fully interactive CLI interface

---

## 📦 Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests
