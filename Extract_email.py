import re
import os

def extract_emails_from_file(input_path, output_path):
    """Extracts all email addresses from a text file and saves them to another file."""
    
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    # Read contents of input file
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Regular expression pattern for email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    # Find all email addresses
    emails = re.findall(email_pattern, text)
    unique_emails = sorted(set(emails))

    # Save to output file
    with open(output_path, 'w', encoding='utf-8') as file:
        for email in unique_emails:
            file.write(email + '\n')

    print(f"✅ Extracted {len(unique_emails)} unique email(s) to {output_path}")

# ----------------------------
# Run the function
# ----------------------------
if __name__ == "__main__":
    input_file = "sample.txt"          # Change this to your actual input file
    output_file = "emails_found.txt"   # Output file to save results
    extract_emails_from_file(input_file, output_file)