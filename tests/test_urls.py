from src.predict import validate_url, predict_url


test_cases = [
    {
        "category": "Normal legitimate URL",
        "url": "https://google.com",
    },
    {
        "category": "HTTPS URL",
        "url": "https://www.wikipedia.org",
    },
    {
        "category": "Long URL",
        "url": "https://example.com/this/is/a/very/long/url/path/for/testing",
    },
    {
        "category": "@ symbol",
        "url": "https://example.com/@user",
    },
    {
        "category": "IP-based URL",
        "url": "http://127.0.0.1",
    },
    {
        "category": "Suspicious keywords",
        "url": "http://secure-login-verify-account.com/login",
    },
    {
        "category": "Many subdirectories",
        "url": "https://example.com/a/b/c/d/e/f/g",
    },
    {
        "category": "Unusual/special characters",
        "url": "https://example.com/%20/test?x=1&y=2",
    },
]


for test in test_cases:
    print("=" * 70)
    print("Category:", test["category"])
    print("URL:", test["url"])

    try:
        result = predict_url(test["url"])

        print("Prediction:", result["label"])

        if result["phishing_score"] is not None:
            print(
                "Phishing Risk Score:",
                f"{result['phishing_score'] * 100:.2f}%"
            )

    except Exception as error:
        print("ERROR:", error)


print("=" * 70)
print("Malformed URL test")

valid, message = validate_url("not a valid url")

print("Valid:", valid)
print("Message:", message)


print("=" * 70)
print("Empty URL test")

valid, message = validate_url("")

print("Valid:", valid)
print("Message:", message)