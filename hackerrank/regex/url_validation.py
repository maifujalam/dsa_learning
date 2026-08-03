import re

def validator(txt):
    pattern=re.compile(r"^(http|https|ftp)://")