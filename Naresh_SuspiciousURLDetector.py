"""
Project: Suspicious URL Detector
Author: Naresh
Purpose: Beginner-friendly defensive cybersecurity project.
Note: This is a rule-based demonstration, not a guaranteed URL safety service.
"""

from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "secure", "account", "banking",
    "password", "confirm", "free", "gift", "urgent"
]
SHORTENING_SERVICES = [
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "ow.ly"
]

def check_url(url):
    """Return a simple risk score and reasons for a URL."""
    text = url.strip()
    if not text:
        return 0, ["No URL entered"]

    candidate = text if "://" in text else "http://" + text
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()
    score = 0
    reasons = []

    if not host:
        return 5, ["URL could not be parsed"]

    if parsed.scheme.lower() != "https":
        score += 1
        reasons.append("Does not use HTTPS")

    if "@" in text:
        score += 2
        reasons.append("Contains '@', which can hide the real destination")

    if len(host) > 30:
        score += 1
        reasons.append("Unusually long domain name")

    if host.count("-") >= 2:
        score += 1
        reasons.append("Domain contains multiple hyphens")

    if sum(ch.isdigit() for ch in host) >= 5:
        score += 1
        reasons.append("Domain contains many digits")

    if any(service in host for service in SHORTENING_SERVICES):
        score += 1
        reasons.append("Uses a URL-shortening service")

    lowered = text.lower()
    found_keywords = [word for word in SUSPICIOUS_KEYWORDS if word in lowered]
    if found_keywords:
        score += 1
        reasons.append("Contains attention-grabbing words: " + ", ".join(found_keywords[:5]))

    if len(text) > 100:
        score += 1
        reasons.append("URL is unusually long")

    return score, reasons


def main():
    print("=" * 48)
    print("        SUSPICIOUS URL DETECTOR")
    print("=" * 48)
    print("Educational rule-based checker. Do not enter private information.")
    url = input("\nEnter a URL to check: ").strip()

    score, reasons = check_url(url)
    print("\nRisk score:", score)

    if score >= 3:
        print("Result: SUSPICIOUS - check carefully before opening.")
    elif score >= 1:
        print("Result: CAUTION - review the URL before opening.")
    else:
        print("Result: No basic warning signs detected.")

    if reasons:
        print("\nReasons:")
        for reason in reasons:
            print("- " + reason)
    else:
        print("- No rules were triggered.")

    print("\nImportant: A low score does NOT prove a URL is safe.")
    print("Never enter passwords or personal details on an untrusted website.")


if __name__ == "__main__":
    main()
