import re

def extract_emails(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        unique_emails = sorted(set(emails))

        print(f"\nFound {len(unique_emails)} unique email(s):\n")
        for email in unique_emails:
            print(email)

        with open("extracted_emails.txt", "w", encoding="utf-8") as output:
            output.write("\n".join(unique_emails))

        print("\nEmails saved to extracted_emails.txt")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    file_path = input("Enter the text file path: ")
    extract_emails(file_path)