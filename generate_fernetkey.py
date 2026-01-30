# Generate a new Fernet encryption key
from cryptography.fernet import Fernet

# Create the key
key = Fernet.generate_key()

# Display the key as a string
print("Your Fernet key:", key.decode())
