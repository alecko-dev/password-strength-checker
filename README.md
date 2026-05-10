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
- [ ] Add repeated-pattern detection
- [ ] Add wordlist checking
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
Pool size: 94
Entropy: 78.65 bits
Strength: Strong

Checks:
- Good length
- Contains a number
- Contains a symbol
- Contains uppercase letters
- Contains lowercase letters
```

## What I Have Learned So Far

So far, this project has helped me understand:

- How to use `getpass` instead of `input()` for hidden password entry
- How `any()` works in Python
- How to check strings for digits, symbols, uppercase, and lowercase characters
- What password entropy means
- Why entropy is measured in bits
- Why a password can look strong mathematically but still be weak in real life

## Current Limitations

This checker is still basic.

Right now, it mostly judges passwords based on length, character variety, and estimated entropy. This means some bad passwords may still appear stronger than they really are.

For example:

```text
aaaaaaaaaaaa
```

This password is long, but it is obviously weak because it is just the same character repeated.

Another example:

```text
Password123!
```

This contains uppercase, lowercase, numbers, and symbols, but it is still predictable because it follows a very common pattern.

I plan to improve this by adding checks for:

- Common passwords
- Repeated characters
- Keyboard patterns
- Dictionary words
- Breached password lists

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