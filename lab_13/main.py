import re

# Sample text containing phone numbers
text = "Call me at 555-1234 or at the office line 555-5678. For emergencies, dial 555-9999."

# Define the regex pattern for phone numbers: three digits, a hyphen, and four digits.
pattern = r"\d{3}-\d{4}"

# Find all matches
phone_numbers = re.findall(pattern, text)

print("Phone Numbers Found:", phone_numbers)

print()

# Sample strings
text1 = "Hello, world! Welcome to regex."
text2 = "Greetings! Hello, how are you?"

# Pattern to check for "Hello"
pattern = r"Hello"

# Using re.match() on text1 (should match)
match1 = re.match(pattern, text1)
print("Using re.match() on text1:")
if match1:
    print("Match found:", match1.group())
else:
    print("No match found.")

# Using re.match() on text2 (should not match because "Hello" is not at the beginning)
match2 = re.match(pattern, text2)
print("\nUsing re.match() on text2:")
if match2:
    print("Match found:", match2.group())
else:
    print("No match found.")

# Using re.search() on text2 (should find "Hello" anywhere in the string)
search_result = re.search(pattern, text2)
print("\nUsing re.search() on text2:")
if search_result:
    print("Found:", search_result.group())
else:
    print("No match found.")

print()

# Sample text with numbers
text = "There are 3 apples, 15 oranges, and 256 bananas in the basket."

# Pattern to match one or more digits
pattern = r"\d+"

# Replace all digit sequences with "NUMBER"
result = re.sub(pattern, "NUMBER", text)

print("Modified Text:", result)

print()

# Sample text containing email addresses
text = "For more info, contact us at support@example.com or sales-info@example.org."

# Regex pattern to match simple email addresses
pattern = r"\b\w+@\w+\.\w+\b"

# Find all email addresses in the text
emails = re.findall(pattern, text)

print("Email Addresses Found:", emails)

print()

# Sample text
text = "An apple a day keeps the doctor away. Even elephants enjoy eating."

# Regex pattern: Words that start with a vowel
pattern = r"\b[aeiou]\w*\b"

# Find all matches with case-insensitivity
vowel_words = re.findall(pattern, text, re.IGNORECASE)

print("Words starting with a vowel:", vowel_words)
