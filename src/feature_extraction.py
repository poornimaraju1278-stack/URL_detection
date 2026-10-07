from urllib.parse import urlparse
import ipaddress
import re


FEATURE_COLUMNS = [
    "url_length",
    "dot_count",
    "has_at",
    "has_https",
    "has_ip",
    "suspicious_keyword_count",
    "hyphen_count",
    "digit_count",
    "special_character_count",
    "path_depth",
    "hostname_length",
]


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "verification",
    "account",
    "secure",
    "update",
    "password",
    "bank",
    "confirm",
    "signin",
    "wallet",
    "free",
    "bonus",
]


def extract_features(url):
    """
    Extract the 11 required URL-based features.

    Returns:
        dict: Features in the exact required order.
    """

    # Handle missing or non-string input safely
    if url is None:
        url = ""
    else:
        url = str(url).strip()

    # Parse URLs even when the scheme is missing
    parse_target = url

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        parse_target = "//" + url

    try:
        parsed = urlparse(parse_target)
        hostname = parsed.hostname or ""
    except ValueError:
        hostname = ""
        parsed = urlparse("")

    # Check whether hostname is an IPv4 address
    has_ip = 0

    try:
        ipaddress.IPv4Address(hostname)
        has_ip = 1
    except ValueError:
        has_ip = 0

    # Convert URL to lowercase for keyword checking
    url_lower = url.lower()

    # Split URL into alphanumeric tokens
    tokens = re.findall(r"[a-z0-9]+", url_lower)

    suspicious_keyword_count = sum(
        1 for token in tokens if token in SUSPICIOUS_KEYWORDS
    )

    # Calculate path depth
    path_parts = [
        part for part in parsed.path.split("/") if part
    ]

    path_depth = len(path_parts)

    # Return features in the exact required order
    features = {
        "url_length": len(url),
        "dot_count": url.count("."),
        "has_at": int("@" in url),
        "has_https": int(parsed.scheme.lower() == "https"),
        "has_ip": has_ip,
        "suspicious_keyword_count": suspicious_keyword_count,
        "hyphen_count": url.count("-"),
        "digit_count": len(re.findall(r"[0-9]", url)),
        "special_character_count": len(
            re.findall(r"[^A-Za-z0-9]", url)
        ),
        "path_depth": path_depth,
        "hostname_length": len(hostname),
    }

    return features