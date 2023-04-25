# Chrome Cookie Extractor

A Python script that extracts cookies from a user's Chrome browser SQLite database. Useful for red teamers and cybersecurity professionals to perform reconnaissance and analyze potential vulnerabilities in web application security.

## Prerequisites

- Python 3.6+
- Google Chrome installed on the system

## Usage

1. Clone the repository:
```git clone https://github.com/yourusername/chrome-cookie-extractor.git```

2. Navigate to the project directory:
```cd chrome-cookie-extractor```

3.Run the script:
```python3 extract_cookies.py```

4.Optional: Extract specific cookies
To extract specific cookies by their name, modify the token_cookie_name variable in the extract_cookies.py script:

```python```
```token_cookie_name = "auth_token"  # Replace this with the actual cookie name for the token```
  
  Replace "auth_token" with the actual cookie name you want to extract.

Disclaimer
This script is provided for educational purposes and authorized use only. Users are responsible for ensuring they have the proper permissions before using this tool. The authors of this script are not responsible for any unauthorized or illegal use.

License
MIT License. See LICENSE for more information.
