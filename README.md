# Password Strength Checker

A simple Python password strength checker that analyses a password based on length, character types, scoring, and estimated entropy.

## Status 
This project is currently a work in progress. I am building it as a beginner cyber security project to practise Python, password security concepts, and clean project documentation.

Progress: 

- [x] Hide password input using `getpass`
- [x] Check password length
- [x] Detect lowercase letters
- [x] Detect uppercase letters
- [x] Detect numbers
- [x] Detect symbols
- [x] Add a basic scoring system
- [x] Calculate estimated password entropy
- [x] Add common password detection
- [ ] Tests
- [ ] Improve final strength rating system

## How It Works

The program checks which character groups are used in the password and uses that to estimate the password's possible character pool.

For example:

- Lowercase letters: 26 characters
- Uppercase letters: 26 characters
- Digits: 10 characters
- Symbols: around 32 characters

The estimated entropy is calculated using:

```text
entropy = password length × log2(pool size)
```

This gives an estimate of how difficult the password may be to brute-force, assuming the password was randomly created.

The checker can also compare the entered password against a common-password wordlist. This helps catch passwords that may look strong mathematically but are already known from leaked or commonly used password lists.

To enable this feature, download the SecLists `10-million-password-list-top-10000.txt` file, rename it to `common-passwords.txt`, and place it inside a `data/` folder.

## Setup

This project uses a common-password wordlist from SecLists.

To enable the common-password check:

1. Download `10-million-password-list-top-10000.txt` from the SecLists repository.
2. Create a folder called `data`.
3. Rename the downloaded file to:

```text
common_passwords.txt
```

4. Place it inside the `data` folder.

Your project should look like this:

```text
password-strength-checker/
├── main.py
├── README.md
├── .gitignore
└── data/
    └── common_passwords.txt
```

The wordlist is ignored by Git using `.gitignore`, so it will not be uploaded to GitHub.

Make sure Python is installed, then run:

## How to Run


```bash
python main.py
```

The program will ask you to enter a password:

```text
Enter Password:
```

The password input is hidden while typing because the project uses Python's `getpass` module.

## Example Output

```text
Password length: 12
Score: 5/5
Entropy: 78.65 bits
Strength: Strong

Checks:
- Good length
- Contains a number
- Contains a symbol
- Contains uppercase letters
- Contains lowercase letters
- Not found in common-passwords list
```

## What I Have Learned So Far

So far, this project has helped me understand:

- How to use `getpass` instead of `input()` for hidden password entry
- How `any()` works in Python
- How to check strings for digits, symbols, uppercase, and lowercase characters
- What password entropy means
- Why entropy is measured in bits
- Why a password can look strong mathematically but still be weak in real life
- How to read external files in Python using `with open(...)`
- Why sets are faster than lists for checking if a password exists in a wordlist
- How to handle missing files without crashing the program
- Why data files should usually be excluded from GitHub using `.gitignore`

## Current Limitations

Right now, it mainly judges passwords using length, character variety, entropy, and common-password detection. This means some weak passwords may still appear stronger than they really are.

For example:

```text
aaaaaaaaaaaa
```

This password is long, but it is weak because it is just the same character repeated.

Another example:

```text
Password123!
```

This contains uppercase letters, lowercase letters, numbers, and symbols, but it is still predictable because it follows a common human pattern.

I plan to improve this by adding checks for:

- Repeated characters
- Keyboard patterns
- Dictionary words
- More common password mutations
- Better strength rating logic

## Planned Improvements

Next steps for this project:

- Add a common password wordlist
- Detect repeated characters like `aaaaaa`
- Detect simple patterns like `123456` or `qwerty`
- Improve the strength rating system
- Add tests
- Refactor the code into functions
- Add clearer user feedback

## Project Goal

The goal of this project is not just to make a working password checker, but to build a small cyber security tool properly.

I want this project to show my progress as I learn Python, security concepts, and how to document technical work clearly.