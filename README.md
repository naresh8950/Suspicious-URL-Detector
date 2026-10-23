# Suspicious URL Detector

**Author:** Naresh Kumar
**Project type:** Beginner-friendly defensive cybersecurity project

## Project description
This Python program checks a URL for simple warning signs that can be associated with phishing or suspicious links. It uses transparent rules such as missing HTTPS, unusually long domains, multiple hyphens, URL-shortener domains, and attention-grabbing words.

This is an educational demonstration, not a machine-learning model or a definitive URL reputation service. A suspicious score does not prove a URL is malicious, and a low score does not prove it is safe.

## Technologies used
- Python 3
- Python standard library (`urllib.parse`)

## Dataset
No external dataset is required to run this rule-based version. For optional further study, a public phishing-URL dataset is available here:
- Phishing Websites dataset (UCI Machine Learning Repository): https://archive.ics.uci.edu/dataset/327/phishing+websites

Use any downloaded dataset only according to its license and terms. This project does not automatically download or process that dataset.

## Requirements
- Python 3.8 or newer
- No third-party libraries

## Setup and run
1. Install Python 3 if it is not already installed.
2. Put `Naresh_SuspiciousURLDetector.py` and `requirements.txt` in the same folder.
3. Open Command Prompt or a terminal in that folder.
4. Run:

   ```bash
   python Naresh_SuspiciousURLDetector.py
   ```

5. Enter a URL when prompted. For a safe demonstration, use a made-up example such as `http://example.com/login`.

`requirements.txt` is included for submission completeness; no `pip install` command is needed because the project uses only built-in Python modules.

## How it works
1. Reads a URL from the user.
2. Parses the URL and checks several simple indicators.
3. Adds points when indicators are found.
4. Prints a caution category and the reasons behind it.

## Limitations and safety
- This is a simple rule-based educational tool.
- It does not visit the URL or verify the website.
- Legitimate websites can trigger warnings, and malicious URLs may not trigger any rules.
- Do not open suspicious links or submit passwords/personal information to them.
