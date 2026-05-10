from getpass import getpass
import string
import math


def load_common_passwords(filepath="data\common-passwords.txt"):
    common_passwords = set()

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                password = line.strip().lower()

                if password:
                    common_passwords.add(password)

    except FileNotFoundError:
        print("Warning: common password file not found.")
        print("Common-password check will be skipped.\n")

    return common_passwords


common_passwords = load_common_passwords()

password = getpass("Enter Password: ")

has_number = any(char in string.digits for char in password)
has_symbol = any(char in string.punctuation for char in password)
has_uppercase = any(char in string.ascii_uppercase for char in password)
has_lowercase = any(char in string.ascii_lowercase for char in password)
has_good_length = len(password) >= 8

is_common = password.lower() in common_passwords

score = 0

if has_good_length:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

pool_size = 0

if has_lowercase:
    pool_size += 26

if has_uppercase:
    pool_size += 26

if has_number:
    pool_size += 10

if has_symbol:
    pool_size += len(string.punctuation)

if pool_size > 0:
    entropy = len(password) * math.log2(pool_size)
else:
    entropy = 0

if is_common:
    strength = "Very Weak"
elif entropy < 28:
    strength = "Very Weak"
elif entropy < 36:
    strength = "Weak"
elif entropy < 60:
    strength = "Medium"
elif entropy < 80:
    strength = "Strong"
else:
    strength = "Very Strong"

print(f"\nPassword length: {len(password)}")
print(f"Score: {score}/5")
print(f"Pool size: {pool_size}")
print(f"Entropy: {entropy:.2f} bits")
print(f"Strength: {strength}")

print("\nChecks:")

if has_good_length:
    print("- Good length")
else:
    print("- Use at least 8 characters")

if has_number:
    print("- Contains a number")
else:
    print("- Add a number")

if has_symbol:
    print("- Contains a symbol")
else:
    print("- Add a symbol")

if has_uppercase:
    print("- Contains uppercase letters")
else:
    print("- Add uppercase letters")

if has_lowercase:
    print("- Contains lowercase letters")
else:
    print("- Add lowercase letters")

if is_common:
    print("- Found in common-passwords list")
else:
    print("- Not found in common-passwords list")