def determine_strength(results):
    if results["breach_count"] is not None and results["breach_count"] > 0:
        return "Compromised"

    if results["is_common"]:
        return "Very Weak"

    entropy = results["entropy"]

    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"


def print_report(results):
    strength = determine_strength(results)

    print(f"\nPassword length: {results['password_length']}")
    print(f"Score: {results['score']}/5")
    print(f"Entropy: {results['entropy']:.2f} bits")
    print(f"Strength: {strength}")

    if results["breach_count"] is None:
        print("Breach check: skipped or failed")
    elif results["breach_count"] > 0:
        print(f"Breach check: found {results['breach_count']:,} times in known breaches")
    else:
        print("Breach check: not found in known breaches")

    print("\nChecks:")

    if results["has_good_length"]:
        print("- Good length")
    else:
        print("- Use at least 8 characters")

    if results["has_number"]:
        print("- Contains a number")
    else:
        print("- Add a number")

    if results["has_symbol"]:
        print("- Contains a symbol")
    else:
        print("- Add a symbol")

    if results["has_uppercase"]:
        print("- Contains uppercase letters")
    else:
        print("- Add uppercase letters")

    if results["has_lowercase"]:
        print("- Contains lowercase letters")
    else:
        print("- Add lowercase letters")

    if results["is_common"]:
        print("- Found in common-passwords list")
    else:
        print("- Not found in common-passwords list")