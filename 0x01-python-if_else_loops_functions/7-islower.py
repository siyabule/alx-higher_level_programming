#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters.
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False"""
    for i in range(97, 123):
        if chr(i) == c:
            return True
        else:
            return False
