import re

def validator(txt):
    pattern=re.compile(r"^(http|https|ftp)://[a-zA-Z0-9.]+(\.[a-zA-Z]{2,})+$")
    return pattern.match(txt)

test_cases = [
    "http://example.com",
    "https://www.domain.org",
    "ftp://server.net/resource",
    "http://localhost",
    "http://127.0.0.1",
    "https://example.com:8080/path/file.html?query=1#fragment",
    "http://sub.domain.co.uk",
    "https://example.io/api/v1/users",
    "htp://wrong.com",
    "example.com",
    "http://",
    "http://.com",
    "http://example..com",
    "http://example,com",
    "http://example.com:abc",
    "://example.com"
]

if __name__ == "__main__":
    for case in test_cases:
        print(validator(case))