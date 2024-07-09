Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
... import string
... 
... def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
...     """
...     Generates a random password based on the specified criteria.
...     
...     Args:
...         length (int): The desired length of the password.
...         include_uppercase (bool): Whether to include uppercase letters.
...         include_lowercase (bool): Whether to include lowercase letters.
...         include_digits (bool): Whether to include digits.
...         include_special (bool): Whether to include special characters.
...     
...     Returns:
...         str: The generated password.
...     """
...     characters = ""
...     if include_uppercase:
...         characters += string.ascii_uppercase
...     if include_lowercase:
...         characters += string.ascii_lowercase
...     if include_digits:
...         characters += string.digits
...     if include_special:
...         characters += string.punctuation
...     
...     password = "".join(random.choice(characters) for _ in range(length))
...     return password
... 
... # Example usage
... length = int(input("Enter the desired password length: "))
... include_uppercase = input("Include uppercase letters? (y/n) ").lower() == "y"
... include_lowercase = input("Include lowercase letters? (y/n) ").lower() == "y"
... include_digits = input("Include digits? (y/n) ").lower() == "y"
... include_special = input("Include special characters? (y/n) ").lower() == "y"
... 
... generated_password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
