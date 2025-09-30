"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = input("Enter your age: ")
phone_number = input("Enter your phone: ")

# Name validation
nameFlag = True
for char in name:
    if not (char.isalpha() or char == " "):
        nameFlag = False
        break

# Age validation
ageFlag = True
try:
    age_int = int(age)
    if age_int < 18 or age_int > 65:
        ageFlag = False
except ValueError:
    ageFlag = False

# Phone validation
phoneFlag = True
if len(phone_number) != 10 or not phone_number.isdigit():
    phoneFlag = False

# Display results
print("\nValidation Results:")
if nameFlag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (contains non-letter characters)")

if ageFlag:
    print(f"Age: Valid ({age} years old)")
else:
    print("Age: Invalid (not a number, or not between 18 and 65)")

if phoneFlag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

# Formatted output
print("\nFormatted Information")
print("Name:", name.upper(), name.lower(), name.capitalize())

if ageFlag and 18 <= age_int <= 30:
    print("Age Group: Young Adult (18-30)")
elif ageFlag:
    print("Age Group: Not Young Adult")

if phoneFlag:
    print("Phone: +66-%s" % phone_number)
