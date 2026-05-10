import hashlib
import urllib.request
import urllib.error


def hash_password_sha1(password: str) -> str:
    password_bytes = password.encode("utf-8")
    sha1_hash = hashlib.sha1(password_bytes).hexdigest().upper()

    return sha1_hash


def split_hash_for_hibp(sha1_hash: str) -> tuple[str, str]:
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    return prefix, suffix


def check_breach_count(password: str):
    sha1_hash = hash_password_sha1(password)
    prefix, suffix = split_hash_for_hibp(sha1_hash)

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "password-strength-checker",
            "Add-Padding": "true",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            response_text = response.read().decode("utf-8")

    except urllib.error.URLError:
        return None
    except TimeoutError:
        return None

    for line in response_text.splitlines():
        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return int(count)

    return 0