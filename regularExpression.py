import re

text = """
Hello, my email is test@example.com and backup is demo.user123@gmail.com
My phone number is 9876543210.
I was born on 26-03-2003.
"""

print("Original Text:\n", text)

# Find all emails
emails = re.findall(r"\w+@\w+\.\w+", text)
print("\nEmails:", emails)

# Find all numbers
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

#  Find phone number (10 digits)
phone = re.findall(r"\d{10}", text)
print("Phone Number:", phone)

#  Find words starting with capital letter
capital_words = re.findall(r"\b[A-Z]\w+", text)
print("Capital Words:", capital_words)

#  Replace numbers with X
replaced_text = re.sub(r"\d", "X", text)
print("\nAfter replacing digits:\n", replaced_text)

#  Search for first email
search_email = re.search(r"\w+@\w+\.\w+", text)
if search_email:
    print("\nFirst Email Found:", search_email.group())

#  Match only at beginning
match_test = re.match(r"Hello", text)
if match_test:
    print("Matched at start:", match_test.group())

# Extract date using groups
date = re.search(r"(\d{2})-(\d{2})-(\d{4})", text)
if date:
    print("\nDate Parts:", date.groups())

#  Using character set
vowels = re.findall(r"[aeiou]", text)
print("Vowels:", vowels[:10])  # showing first 10 only

#  Using compile (reusable pattern)
pattern = re.compile(r"\d+")
print("\nUsing compile:", pattern.findall(text))