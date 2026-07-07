password = input("Enter password: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

special = "!@#$%^&*()?><"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special:
        has_special = True

if length < 8:
    print("PASSWORD IS WEAK\nEnter password of atleast 8 characters")
elif has_upper and has_lower and has_digit and has_special:
    print("STRONG PASSWORD")
elif (has_upper or has_lower) and has_digit:
    print("MEDIUM PASSWORD\nEnter password having special characters")
else:
    print("WEAK PASSWORD")