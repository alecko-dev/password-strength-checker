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