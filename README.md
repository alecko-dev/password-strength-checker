# Password Strength Checker

A Python password strength checker that analyses passwords using character variety, estimated entropy, common-password detection, and breach checking through the Have I Been Pwned Pwned Passwords API.

This project is being built as a practical cyber security learning project. The goal is not just to make a working password checker, but to build it properly with clear code structure, documentation, and tests.

## Project Status

This project is currently a work in progress.

The main checker is functional and can:

- Analyse password length and character variety
- Estimate password entropy
- Check against a common-password wordlist
- Check whether a password appears in known breaches using Have I Been Pwned
- Handle missing wordlists or failed network checks without crashing
- Run unit tests for core modules

## Progress Tracker

### Core Features

- [x] Hide password input using `getpass`
- [x] Check password length
- [x] Detect lowercase letters
- [x] Detect uppercase letters
- [x] Detect numbers
- [x] Detect symbols
- [x] Add a basic scoring system
- [x] Calculate estimated password entropy
- [x] Add common-password detection using a SecLists wordlist
- [x] Add Have I Been Pwned breach check
- [x] Add thousands separators for breach counts
- [x] Refactor code into separate modules
- [x] Add unit tests
- [ ] Add repeated-character detection
- [ ] Add keyboard-pattern detection
- [ ] Add dictionary-word detection
- [ ] Improve final strength rating logic
- [ ] Add command-line options

### Documentation / Repo Setup

- [x] Create initial README
- [x] Add project goals
- [x] Add feature checklist
- [x] Add `.gitignore`
- [x] Exclude downloaded wordlist from GitHub
- [x] Add project structure
- [x] Add testing instructions
- [ ] Add screenshots or terminal output examples
- [ ] Add final polished README after the project is complete

## Why I Am Building This

I am studying mechanical engineering, but I also have a strong interest in cyber security.

I chose this project because password strength is a simple but important security topic. It gives me a practical way to improve my Python skills while learning about entropy, wordlists, hashing, APIs, breach data, and secure tool design.

This project also helps me build a public portfolio showing that I can structure code, document my work, and improve a project over time.

## Features

The checker currently analyses:

- Password length
- Lowercase letters
- Uppercase letters
- Numbers
- Symbols
- Estimated entropy in bits
- Whether the password appears in a common-password wordlist
- Whether the password appears in known breaches
- A final strength rating

## Project Structure

```text
password-strength-checker/
├── main.py
├── analysis.py
├── wordlist.py
├── verdict.py
├── breach_check.py
├── README.md
├── .gitignore
├── data/
│   └── common_passwords.txt
└── tests/
    ├── test_analysis.py
    ├── test_wordlist.py
    ├── test_verdict.py
    └── test_breach_check.py
```

## File Overview

### `main.py`

Runs the program.

It loads the common-password wordlist, asks the user for a password, sends the password through the analysis logic, and prints the final report.

### `analysis.py`

Handles the main password analysis logic.

This includes:

- Character class detection
- Pool size calculation
- Entropy calculation
- Common-password checking
- Breach-check result handling

### `wordlist.py`

Loads the common-password wordlist from the `data/` folder.

The wordlist is stored as a set so password lookups are fast.

### `verdict.py`

Decides the final password strength rating and prints the user-facing report.

### `breach_check.py`

Handles the Have I Been Pwned breach check.

It hashes the password locally, sends only the first five characters of the SHA-1 hash to the API, then checks the returned hash suffixes locally.

### `tests/`

Contains unit tests for the main project modules.

## How It Works

The program checks which character groups are used in the password and uses that to estimate the possible character pool.

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

## Common-Password Check

The checker can compare the entered password against a common-password wordlist.

This helps catch passwords that may look decent mathematically but are still weak because they are commonly used.

For example:

```text
Password123!
```

This password has uppercase letters, lowercase letters, numbers, and a symbol, but it follows a very predictable pattern.

If a password appears in the common-password list, it is treated as very weak even if the entropy score looks high.

## Breach Check

The checker also uses the Have I Been Pwned Pwned Passwords API to check whether a password has appeared in known data breaches.

The password itself is never sent over the network.

Instead, the program:

1. Hashes the password locally using SHA-1
2. Sends only the first five characters of the hash to the API
3. Receives a list of matching hash suffixes
4. Checks locally whether the rest of the hash appears in that list

This means the actual password never leaves the user's computer.

If the password is found in known breaches, the checker marks it as:

```text
Compromised
```

If the API is unavailable or the user has no internet connection, the tool does not crash. It skips the breach check and continues using the other password checks.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/password-strength-checker.git
cd password-strength-checker
```

### 2. Add the common-password wordlist

This project uses a common-password wordlist from SecLists.

To enable common-password detection:

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

## How to Run

Make sure Python is installed, then run:

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
Strength: Compromised
Breach check: found 52,256,179 times in known breaches

Checks:
- Good length
- Contains a number
- Contains a symbol
- Contains uppercase letters
- Contains lowercase letters
- Found in common-passwords list
```

## Running Tests

This project uses Python's built-in `unittest` framework.

To run all tests:

```bash
python -m unittest discover -s tests
```

To run one test file:

```bash
python -m unittest tests/test_analysis.py
```

or:

```bash
python -m unittest tests/test_breach_check.py
```

If all tests pass, the output should look similar to:

```text
Ran 20 tests in 0.123s

OK
```

## What I Have Learned So Far

So far, this project has helped me understand:

- How to use `getpass` instead of `input()` for hidden password entry
- How `any()` works in Python
- How to check strings for digits, symbols, uppercase, and lowercase characters
- What password entropy means
- Why entropy is measured in bits
- How to read external files in Python using `with open(...)`
- Why sets are faster than lists for checking if a password exists in a wordlist
- How to handle missing files without crashing the program
- Why data files should usually be excluded from GitHub using `.gitignore`
- How to split a Python script into separate modules
- How to hash passwords locally using Python's `hashlib`
- How the Have I Been Pwned k-anonymity model works
- Why SHA-1 is used here as a lookup format, not as secure password storage
- How to make HTTP requests using `urllib`
- How to handle failed API requests gracefully
- How to write basic unit tests using `unittest`
- How to test code that would normally make network requests

## Current Limitations

This checker is still basic.

Right now, it mainly judges passwords using length, character variety, entropy, common-password detection, and breach detection.

Some weak passwords may still appear stronger than they really are.

For example:

```text
aaaaaaaaaaaa
```

This password is long, but it is weak because it is just the same character repeated.

Another example:

```text
Qwerty123!
```

This contains multiple character types, but it is still predictable because it uses a common keyboard pattern.

These are planned improvements.

## Planned Improvements

Next steps for this project:

- Detect repeated characters like `aaaaaa`
- Detect keyboard patterns like `qwerty` or `asdf`
- Detect simple number sequences like `123456`
- Improve the strength rating system
- Add command-line options
- Add an offline mode that skips the breach check
- Add clearer user feedback
- Add screenshots or terminal output examples to the README
- Keep expanding the test suite

## Important Note

This tool is for learning and basic password analysis.

It should not be treated as a perfect password security system. Real password strength depends on many factors, including whether the password is reused, whether it has appeared in breaches, whether it follows common patterns, and whether the user stores it safely.

A password manager and unique passwords for each account are still recommended.

## Project Goal

The goal of this project is not just to make a working password checker.

The goal is to build a small cyber security tool properly by practising:

- Python programming
- Code structure
- Security concepts
- Documentation
- Testing
- Iterative improvement

This project is part of my broader interest in cyber security, practical security tools, and building a stronger technical portfolio.