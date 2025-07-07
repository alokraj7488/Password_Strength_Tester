import hashlib
import requests
import re

def analyze_password_strength(password):
    # Initialize strength score
    strength_score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Your password is too short. It should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Your password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Your password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Your password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Your password should include at least one special character (!, @, #, etc.).")

    # Check for common patterns (e.g., "12345", "abcdef")
    if re.search(r'(123|abc|qwerty)', password.lower()):
        feedback.append("Your password contains a common pattern. Avoid using predictable sequences.")
        strength_score -= 1

    # Check for repeated characters (e.g., "aaaa")
    if re.search(r'(.)\1\1', password):
        feedback.append("Your password contains repeated characters. Avoid repeating the same character multiple times.")
        strength_score -= 1

    # Determine overall strength
    if strength_score <= 2:
        strength = "Weak"
    elif strength_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


def check_password_leak(password):
    # Step 1: Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Step 2: Extract the first 5 characters of the hash (k-anonymity)
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    # Step 3: Query the Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        return "Error: Unable to check password against the database."
    
    # Step 4: Parse the response and check if the password hash exists
    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return f"Warning: This password has been leaked {count} times!"
    
    # If no match found, the password is safe
    return "Good news! This password has not been leaked."


def main():
    print("Welcome to the Password Strength & Leak Checker!")
    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("Thank you for using the Password Strength & Leak Checker. Goodbye!")
            break
        
        # Analyze password strength
        strength, feedback = analyze_password_strength(password)
        
        # Check if the password has been leaked
        leak_status = check_password_leak(password)
        
        # Display results
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(f" - {suggestion}")
        else:
            print("Great job! Your password meets all the complexity requirements.")
        
        print(f"\nLeak Status: {leak_status}\n")


if __name__ == "__main__":
    main()
