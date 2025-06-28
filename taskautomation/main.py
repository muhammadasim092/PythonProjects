import os 
import re

input_file = "email.txt"
output_file = "email_extracted.txt"

if not os.path.isfile(input_file):
    print("The file does not exist")

else:
    with open(input_file, 'r') as file:
        content = file.read()
        
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(email_pattern, content)
    
    unique_emails = sorted(set(emails))

    
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')
            
print(f"Extracted {len(unique_emails)} unique emails and saved them to {output_file}")