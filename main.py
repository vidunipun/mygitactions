import os
import subprocess

# Get the secret from the GitHub Actions environment
secret = os.getenv("MY_SECRET")

# Print the secret value
print(f"The secret value is: {secret}")

# Run the main.py file
subprocess.run(["python", "main.py"])
