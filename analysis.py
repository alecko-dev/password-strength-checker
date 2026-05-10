import string
import math


def analyse_character_classes(password):
    return {
        "has_lowercase": any(char in string.ascii_lowercase for char in password),
        "has_uppercase": any(char in string.ascii_uppercase for char in password),
        "has_number": any(char in string.digits for char in password),
        "has_symbol": any(char in string.punctuation for char in password),
    }


def calculate_pool_size(character_classes):
    pool_size = 0

    if character_classes["has_lowercase"]:
        pool_size += 26

    if character_classes["has_uppercase"]:
        pool_size += 26

    if character_classes["has_number"]:
        pool_size += 10

    if character_classes["has_symbol"]:
        pool_size += len(string.punctuation)

    return pool_size


def calculate_entropy(password, pool_size):
    if pool_size > 0:
        return len(password) * math.log2(pool_size)

    return 0


def analyse_password(password, common_passwords):
    character_classes = analyse_character_classes(password)

    has_good_length = len(password) >= 8
    is_common = password.lower() in common_passwords

    score = sum([
        has_good_length,
        character_classes["has_lowercase"],
        character_classes["has_uppercase"],
        character_classes["has_number"],
        character_classes["has_symbol"],
    ])

    pool_size = calculate_pool_size(character_classes)
    entropy = calculate_entropy(password, pool_size)

    return {
        "password_length": len(password),
        "has_good_length": has_good_length,
        "has_lowercase": character_classes["has_lowercase"],
        "has_uppercase": character_classes["has_uppercase"],
        "has_number": character_classes["has_number"],
        "has_symbol": character_classes["has_symbol"],
        "score": score,
        "pool_size": pool_size,
        "entropy": entropy,
        "is_common": is_common,
    }