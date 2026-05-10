from getpass import getpass
from wordlist import load_common_passwords
from analysis import analyse_password
from verdict import print_report


def main():
    common_passwords = load_common_passwords()

    password = getpass("Enter Password: ")

    results = analyse_password(password, common_passwords)

    print_report(results)


if __name__ == "__main__":
    main()