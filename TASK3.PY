import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Read text from input file
with open(input_file, "r") as file:
    content = file.read()

# Regular expression for email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Write extracted emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("✅ Email extraction completed.")
print(f"📁 Extracted emails saved to '{output_file}'")
