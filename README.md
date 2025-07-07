# Password Strength & Leak Checker 🔐

A simple yet powerful Python tool that checks:
- The strength of your password based on complexity rules
- Whether your password has been leaked using the [Have I Been Pwned](https://haveibeenpwned.com/ ) API
  
🔒 Your privacy is protected: Only a part of the hashed password is sent to the server (k-anonymity model).

---

#🧩 Features
✔️ Password complexity analysis with actionable feedback
🔍 Secure breach detection without sending full password
💬 Interactive CLI interface
📦 No external databases required
🛡️ Fully compliant with k-anonymity best practices


#🛠️ Technologies Used
Python 3
Standard Libraries: hashlib, re, requests
Third-party API: Have I Been Pwned Passwords API

## 🚀 How to Use

### ✅ Clone the Repository

```bash
git clone  https://github.com/YOUR_USERNAME/password-strength-checker.git 
cd password-strength-checker


🛡️ Security Note
This tool uses SHA-1 hashing and the k-anonymity method , so only the first 5 characters of the hash are sent to the API server. This ensures your password remains private and secure.


