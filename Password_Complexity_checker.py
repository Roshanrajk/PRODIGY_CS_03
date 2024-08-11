import re

def check_password_complexity(password):
    # Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for uppercase and lowercase letters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Password must contain both uppercase and lowercase letters."
    
    # Check for digits
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."
    
    # Check for special characters
    special_characters = r"[!@#$%^&*()\-_+=\\|[\]{};:/?.>,<]"
    if not re.search(special_characters, password):
        return "Password must contain at least one special character from: ! @ # $ % ^ & * ( ) - _ = + \\ | [ ] { } ; : / ? . >"
    
    return "Your password is strong!"

# Example usage
password = input("Enter a password to check its strength: ")
result = check_password_complexity(password)
print(result)
