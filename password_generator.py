import random
import string

def generate_password(length):
    choices = choices = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# This gives:
# abc...xyz + ABC...XYZ + 0123456789 + !@#$%^&*...
    password = []
    while len(password) < length:
        random_char = random.choice(choices)
        password.append(random_char)
    return "".join(password)
   #password = [random.choice(choices) for _ in range(length)] 
print(generate_password(10)) 

import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Start with lowercase
    choices = string.ascii_lowercase
    
    # Add based on options
    if use_uppercase:
        choices += string.ascii_uppercase
    if use_digits:
        choices += string.digits
    if use_special:
        choices += string.punctuation
    
    # Generate password
    password = [random.choice(choices) for _ in range(length)]
    return "".join(password)

# Examples:
print(generate_password(10))                               # All characters
print(generate_password(10, use_special=False))            # No special chars
print(generate_password(10, use_uppercase=False))          # Only lowercase + digits + special
print(generate_password(10, use_digits=False, use_special=False))  # Only letters   
